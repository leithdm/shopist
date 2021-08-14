from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.store, name="home"),
    path('product/', views.productDetails, name="product"),
]
