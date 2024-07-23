from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User , AbstractUser
# Create your models here.

class nations(models.Model):
    name = models.CharField(max_length=50 , default='')
    code = models.CharField(max_length=3 , default='')

    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=100 , default='')
    code = models.CharField(max_length=3 , default='')

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_items = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Cart of {self.user.username} '

    def update_total_items(self):
        print("Updating total items...")  # Debugging print
        self.total_items = sum(item.quantity for item in self.items.all())
        print(f"New total items: {self.total_items}")  # Debugging print
        self.save()

    def total_price(self):
        return sum(item.total_price for item in self.items.all())


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Season(models.Model):
    season = models.CharField(max_length=200)

    def __str__(self):
        return self.season
    

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    season = models.ForeignKey(Season , on_delete=models.CASCADE)
    image = models.FileField(upload_to='static/image/' , blank=True , null=True)
    added_by = models.ForeignKey(User , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items'  , default='')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10 , null=True , default='')

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
    @property
    def total_price(self):
        return self.quantity * self.product.price
    
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT , null=True , default='')
    subject = models.CharField(max_length=155 , default='')
    message = models.TextField(default='message')
    phone = models.CharField(max_length=12 , default='')
    email = models.EmailField(default='')
    Custom_id = models.PositiveIntegerField(unique=True , null=True , blank=True)
    def save(self,*args , **kwargs):
        if self.Custom_id is None:
            last_customer = Contact.objects.all().order_by('Custom_id').last()
            if last_customer :
                self.Custom_id = last_customer.Custom_id + 1
            else:
                self.Custom_id = 1
        super().save(*args , **kwargs)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=20 , default='')
    city = models.ForeignKey(City, on_delete=models.CASCADE , default='')
    phone = models.CharField(max_length=15 , default='')
    address = models.CharField(max_length=100 , default='')
    image = models.FileField(upload_to='static/image', blank=True)
    cart = models.ForeignKey(Cart , on_delete=models.SET_NULL , default='' , null=True)    
    nationality = models.ForeignKey(nations , on_delete=models.SET_DEFAULT , default=51)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    size = models.CharField(max_length=5)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"

    @property
    def total_price(self):
        return self.quantity * self.product.price
    