from django.urls import path
from .views import *

app_name = 'crm'

urlpatterns = [
    path('' , HomeView.as_view() , name='home'),
    path('crm/' , CrmView.as_view() , name='contact'),
    path('user/' , UserListView.as_view() , name='user'),
    path('detail/<int:pk>/' , CrmDetailView.as_view(),name='crm-detail'),
    path('detail/<int:pk>/delete/' , DeleteCrmView.as_view() , name='delete'),
    path('orders/' , Ordersview.as_view() , name='order'),
    path('products/' , ProductsListView.as_view() , name='product'),
    path('create/' , ProductsCreateView.as_view() , name='create'),
    path('products/<int:pk>/' , ProductsDetailView.as_view() , name='product-details'),
]