# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model
# from .models import UserModel

# User = get_user_model()

# @receiver(post_save, sender=User)
# def create_or_update_user_model(sender, instance, created, **kwargs):
#     if created:
#         UserModel.objects.create(user=instance)
#     else:
#         instance.usermodel.save()

# # Connect the signal in your apps.py or any other place where it gets imported when Django starts.
