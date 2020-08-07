from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'home.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def newpage(request):
    return HttpResponse("This is demo page.")
