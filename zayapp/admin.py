from django.contrib import admin
from .models import Category , Products , Season , Cart ,CartItem , City , UserProfile , nations , Contact , Order

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' , 'id']
    ordering = ['id']

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['season' , 'id']
    ordering = ['id']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price' , 'category' , 'season' , 'added_by' , 'id']
    ordering = ['id']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user' , 'total_items']
    ordering = ['id']

@admin.register(CartItem)
class ClassItemAdmin(admin.ModelAdmin):
    list_display = ['cart' , 'product' , 'quantity' , 'size']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name' , 'code' , 'id']
    ordering = ['id']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user' , 'city' , 'address' , 'phone' ,'id']
    ordering = ['id']

@admin.register(nations)
class nationsAdmin(admin.ModelAdmin):
    list_display = ['name' , 'code' , 'id']
    ordering = ['id']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user' , 'subject' ,  'id']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'id' , 'created_at']