from django.shortcuts import get_object_or_404, redirect, render
from store.models import Category, Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


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
    return render(request, 'checkout/index.html', dict(cart_items=cart_items, total=total, counter=counter))


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