from django.contrib import admin
from store.models import Category, Product
from .models import Cart, CartItem

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
