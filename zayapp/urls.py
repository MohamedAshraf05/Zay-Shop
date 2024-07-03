from django.urls import path
from .views import *
from . import views

app_name = 'zay'
urlpatterns = [
    path('' , HomeView.as_view() , name='home'), # homePage view only for introducing the website
    path('shop/' , ProductView.as_view() , name='shop'), # All products in the database
    path('shop/<int:pk>/' , SingleProduct.as_view() , name='single'), # Single product view
    path('cart/' , CartDetailView.as_view() , name='cart'), # Cart View 
    path('cart/<int:pk>/delete/' , CartItemDeleteView.as_view() , name='delete'), # Deleting products
    path('shop/men/' , MenView.as_view() , name='men'), # filtering the products to the men products only 
    path('shop/women/' , WomenView.as_view() , name='women'), # filtering the products to the women products only
    path('login/' , CustomerLoginView.as_view() , name='login'), # Login form view
    path('register/' , CustomerRegisterView.as_view() , name='register'), # registration form 
    path('logout/' , views.Logout , name='logout')   
]