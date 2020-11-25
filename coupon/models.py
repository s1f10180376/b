from django.db import models
from django.utils import timezone

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
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
