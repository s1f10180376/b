from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coupon/get/<int:shop_id>', views.get, name='get'),
    path('coupon/detail/<int:coupon_id>', views.detail, name='detail'),
    path('coupon/use/<int:coupon_id>', views.use, name='use'),
]
