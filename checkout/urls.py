from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>', views.add_cart, name='add_cart'),

]