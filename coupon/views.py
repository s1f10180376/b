from django.shortcuts import render
from django.utils import timezone
import datetime
from coupon.models import Shop, Coupon

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    """home screen"""
    coupons = Coupon.objects.all()
    today = timezone.now().date()
    for c in coupons: # delete expired coupons
        if c.limit < today:
            c.delete()
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
        user = request.user,
        shop=shop)
    context = {
        'coupon' : coupon,
        'shop' : shop
    }
    return render(request, 'coupon/get.html', context)

@login_required
def detail(request, coupon_id):
    coupon = Coupon.objects.get(pk=coupon_id)
    context = {
        'coupon' : coupon,
    }
    return render(request, 'coupon/detail.html', context)

@login_required
def use(request, coupon_id):
    try:
        coupon = Coupon.objects.get(pk=coupon_id)
        context = {
            'name' : coupon.coupon_name,
            'content' : coupon.coupon_content,
            'shop' : coupon.shop.shop_name
        }
        coupon.delete()
    except Coupon.DoesNotExist:
        context = {
            'name' : 'このクーポンは存在しません',
            'content' : 'すでに使用済みです',
            'shop' : ''
        }
    return render(request, 'coupon/use.html', context)
