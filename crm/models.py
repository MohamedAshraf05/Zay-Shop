from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class UserModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    CustomId = models.PositiveBigIntegerField(unique=True , null=True , blank=True)

    def save(self,*args , **kwargs):
        if self.CustomId is None:
            last_customer = UserModel.objects.all().order_by('CustomId').last()
            if last_customer :
                self.Custom_id = last_customer.CustomId + 1
            else:
                self.CustomId = 1
        super().save(*args , **kwargs)