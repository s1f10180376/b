from django.shortcuts import render
from django.utils import timezone
import datetime
from coupon.models import Shop, Coupon

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    """home screen"""
    coupons = Coupon.objects.filter(user=request.user.id)
    today = timezone.now().date()
    for c in coupons: # delete expired coupons
        if c.limit < today:
            c.delete()
    coupons = Coupon.objects.filter(user=request.user.id)
    context = {
        'coupons' : coupons
    }
    return render(request, 'coupon/home.html', context)

@login_required
def get(request, shop_id):
    """get a coupon"""
    now = timezone.now()
    shop = Shop.objects.get(pk=shop_id)

    coupons = Coupon.objects.filter(shop = shop_id)
    for c in coupons:
        if c.date.date() == now.date():
            context = {
                'comment': "既に取得済みのクーポンです。",
                'coupon' : c,
                'shop' : shop
            }
            return render(request, 'coupon/get.html', context)

    coupon = Coupon.objects.create(
        coupon_name=shop.coupon_name, 
        coupon_content=shop.coupon_content,
        term=shop.term, 
        limit=(now + datetime.timedelta(weeks=shop.term)).date(), 
        user = request.user,
        shop=shop)
    context = {
        'comment': "クーポンを取得しました。",
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
    coupon = Coupon.objects.get(pk=coupon_id)
    context = {
        'coupon' : coupon,
    }
    coupon.delete()
    return render(request, 'coupon/use.html', context)

@login_required
def account(request):
    return render(request, 'coupon/account.html')
