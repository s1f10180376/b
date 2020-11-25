from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get/<int:shop_id>', views.get, name='get'),
]
