from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<slug:category_slug>', views.home, name="categorized_products"),
    path('product/', views.productDetails, name="product"),
]
