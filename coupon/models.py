from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=128)
    coupon_name = models.CharField(max_length=128)
    coupon_content = models.TextField(default="")
    term = models.IntegerField(null=True)

class Coupon(models.Model):
    coupon_name = models.CharField(max_length=128)
    coupon_content = models.TextField(default="")
    date = models.DateTimeField(default=timezone.now)
    term = models.IntegerField(null=True)
    limit = models.DateField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default="")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
