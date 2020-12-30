from django.urls import path
from django.contrib import admin
from . import views

#app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
