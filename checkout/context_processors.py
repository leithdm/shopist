from checkout.models import CartItem, Cart

#used to find the corresponding cart object
from checkout.views import get_cart_id


''' Returns the number of items in the cart '''
def counter(request):
    item_count = 0 

    #condition to check if admin is part of the requested path. If so, return empty dict
    if 'admin' in request.path:
        return {}
    #otherwise we will calculate the item count from the cart
    else:
        try:
            cart = Cart.objects.filter(cart_id=get_cart_id(request))
            #then find the corresponding cartItems, with a [:1] to return a single cartItems object
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            #loop through each cartItem and get its qty
            for cart_item in cart_items:
                item_count += cart_item.quantity
        #if there are no cartItems in the current session, the item count should be 0
        except Cart.DoesNotExist:
            item_count = 0 
        #function returns a dictionary which contains the item count variable
        return dict(item_count=item_count)
