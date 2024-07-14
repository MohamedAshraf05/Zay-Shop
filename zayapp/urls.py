from django.urls import path
from .views import *
from . import views

app_name = 'zay'
urlpatterns = [
    path('' , HomeView.as_view() , name='home'), # homePage view only for introducing the website
    path('shop/' , ProductView.as_view() , name='shop'), # All products in the database
    path('shop/buy/<int:pk>/' , orderView.as_view() , name='order'),
    path('shop/<int:pk>/' , SingleProduct.as_view() , name='single'), # Single product view
    path('cart/' , CartDetailView.as_view() , name='cart'), # Cart View 
    path('cart/<int:pk>/delete/' , CartItemDeleteView.as_view() , name='delete'), # Deleting products
    path('shop/men/' , MenView.as_view() , name='men'), # filtering the products to the men products only 
    path('shop/women/' , WomenView.as_view() , name='women'), # filtering the products to the women products only
    path('login/' , CustomerLoginView.as_view() , name='login'), # Login form view
    path('register/' , CustomerRegisterView.as_view() , name='register'), # registration form 
    path('logout/' , views.Logout , name='logout'), # logout url without view
    path('register/form' , UserProfileFormView.as_view() , name='form' ), # Form for taking more informations about the user 
    path('profile/' , UserProfileDetailView.as_view() , name='profile'), # profile view for the user 
    path('profile/update/' , UserProfileUpdateView.as_view() , name='update'), # Updating the profile view of the user if he wanted
    path('about/' , AboutView.as_view() , name='about'), # About view for the website 
    path('contact/' , ContactFormView.as_view() , name='contact'), # let the users to contact the admins or the owner of the site 
]