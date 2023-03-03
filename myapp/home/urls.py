from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.base, name="base"),
    path('shop', views.shop, name="shop"),
    path('blog', views.blog, name="blog"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('cart', views.cart, name="cart"),
    path('sproduct', views.sproduct, name="sproduct"),
]
