from django.shortcuts import render, get_object_or_404, redirect
from checkout.models import Order, OrderItem
from store.models import Review
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage


@login_required(redirect_field_name='next', login_url='login')
def profile(request):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.filter(emailAddress=email)
        reviews = Review.objects.filter(user=request.user)    
    return render(request, 'profiles/profile.html', {'order_details': order_details, 'reviews': reviews})


@login_required(redirect_field_name='next', login_url='login')
def viewOrder(request, order_id):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order = Order.objects.get(id=order_id, emailAddress=email)
        order_items = OrderItem.objects.filter(order=order)
    return render(request, 'profiles/order_detail.html', {'order': order, 'order_items': order_items})


@login_required(redirect_field_name='next', login_url='login')
def deleteReview(request, review_id):
    if request.user.is_authenticated:
        review_to_delete = Review.objects.get(id=review_id)
        review_to_delete.delete()
        reviews = Review.objects.filter(user=request.user)    
    return render(request, 'profiles/profile.html', {'reviews': reviews})
