from django.shortcuts import render

# Create your views here.
def home(request):
    """home screen"""
    return render(request, 'coupon/home.html')
