from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get/<int:shop_id>', views.get, name='get'),
    path('detail/<int:coupon_id>', views.detail, name='detail'),
    path('use/<int:coupon_id>', views.use, name='use'),
]
