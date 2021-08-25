from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<slug:category_slug>', views.home, name="categorized_products"),
    path('category/<slug:category_slug>/<slug:product_slug>', views.productDetails, name="product_detail"),
    path('search/', views.search, name='search'),
]
