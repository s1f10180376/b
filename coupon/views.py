from django.shortcuts import render
from django.utils import timezone
import datetime
from coupon.models import Shop, Coupon

from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    """home screen"""
    coupons = Coupon.objects.all()
    context = {
        'coupons' : coupons
    }
    return render(request, 'coupon/home.html', context)

@login_required
def get(request, shop_id):
    """get a coupon"""
    shop = Shop.objects.get(pk=shop_id)
    coupon = Coupon.objects.create(
        coupon_name=shop.coupon_name, 
        coupon_content=shop.coupon_content,
        term=shop.term, 
        limit=(timezone.now() + datetime.timedelta(weeks=shop.term)).date(), 
        shop=shop)
    context = {
        'coupon' : coupon,
        'shop' : shop
    }
    return render(request, 'coupon/get.html', context)
