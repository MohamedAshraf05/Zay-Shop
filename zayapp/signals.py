from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import CartItem, Cart

@receiver(post_delete, sender=CartItem)
def update_cart_total_items_on_delete(sender, instance, **kwargs):
    cart = instance.cart
    print(f"Updating cart total items for cart: {cart}")  # Debugging print
    cart.update_total_items()
    print(f"Cart total items after update: {cart.total_items}")  # Debugging print
