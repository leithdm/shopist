from django.shortcuts import get_object_or_404, redirect, render
from store.models import Category, Product
from .models import Cart, CartItem, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import stripe


''' Get the cart_id '''
def get_cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


''' Add a product to the cart, and update its quantity '''
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=get_cart_id(request))
    
    # create an empty cart if no cart exists in the session. Use session_key as id. 
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = get_cart_id(request)
        )
        cart.save()
    # if cartItem exists, update its qty
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        #only add to cart if have available stock
        if cart_item.quantity < cart_item.product.stock:
                cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        # create a new cartItem object from the product and cart object, set qty to 1
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart, 
        )
        cart_item.save()

        # will update all cart items in current session
    return redirect('cart_detail')


''' Retrieve all cartItems in the current session, and calculate total cost of all cart items in the cart'''
def cart_detail(request, total=0, counter=0, cart_items=None):
    # try to get the Cart object from the current session
    try:
        cart = Cart.objects.get(cart_id=get_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        # calculate total cost of items in cart
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            # total number of items in the cart
            counter += cart_item.quantity
    # if no cart is present in the session, we ignore it
    except ObjectDoesNotExist:
        pass

    #stripe API
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'Shopis-Store - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == "POST":
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingCity = request.POST['stripeBillingAddressCity']
            billingCountry = request.POST['stripeBillingAddressCountryCode']
            shippingName = request.POST['stripeShippingName']
            shippingAddress1 = request.POST['stripeShippingAddressLine1']
            shippingCity = request.POST['stripeShippingAddressCity']
            shippingCountry = request.POST['stripeShippingAddressCountryCode']
            billingPostcode = request.POST['stripeBillingAddressZip']
            shippingPostcode = request.POST['stripeShippingAddressZip']
            customer = stripe.Customer.create(
                email=email,
                source=token
            )
            charge = stripe.Charge.create(
                amount=stripe_total,
                currency='eur',
                description=description,
                customer=customer.id
            )
            try:
                order_details = Order.objects.create(
                    token=token,
                    total=total,
                    emailAddress=email,
                    billingName=billingName,
                    billingAddress1=billingAddress1,
                    billingCity=billingCity,
                    billingPostcode=billingPostcode,
                    billingCountry=billingCountry,
                    shippingName=shippingName,
                    shippingAddress1=shippingAddress1,
                    shippingCity=shippingCity,
                    shippingPostcode=shippingPostcode,
                    shippingCountry=shippingCountry
                )
                #after receiving order, save to the database
                order_details.save()
                for order_item in cart_items:
                    or_item = OrderItem.objects.create(
                        product=order_item.product.name,
                        quantity=order_item.quantity,
                        price=order_item.product.price,
                        order=order_details
                    )
                    or_item.save()

                    #reduce the stock that we have
                    products = Product.objects.get(id=order_item.product.id)
                    products.stock = int(order_item.product.stock - order_item.quantity)
                    products.save()
                    order_item.delete()
                    print('**The order has been successfully created**')
                return redirect('home')
            #if the object does not exist, simply do a pass to ignore it
            except ObjectDoesNotExist:
                pass
        except stripe.error.CardError as e:
            return False, e
    return render(request, 'checkout/index.html', dict(cart_items=cart_items, total=total, counter=counter, data_key=data_key, stripe_total=stripe_total, description=description))


''' Remove a cartItem from the cart '''
def cart_removeItem(request, product_id):
    cart = Cart.objects.get(cart_id=get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    #if qty is >1, then decrement by 1
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    #if qty=0, remove it from the cart
    else:
        cart_item.delete()
    #redirect to 'cart_detail' to update the UI
    return redirect('cart_detail')


''' Trash a cartItem from the cart '''
def cart_trashItem(request, product_id):
    cart = Cart.objects.get(cart_id=get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')