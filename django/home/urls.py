from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("index", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("phone",views.phone,name="phone"),
    path("cart", views.cart,name="cart" ),
    path("",views.login,name="login"),
    path("laptop", views.laptop,name="laptop"),
    path("shop1", views.shop1,name="shop1"),
]