from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>', views.cart_removeItem, name='cart_removeItem'),
    path('trash/<int:product_id>', views.cart_trashItem, name='cart_trashItem'),

]