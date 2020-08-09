from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('hello world')

def about(request):
    return render(request, 'details/about.html')

def contact(request):
    return render(request, 'details/contact.html')

def returns(request):
    return render(request, 'details/returns.html')

def privacy_policy(request):
    return render(request, 'details/privacy-policy.html')

def faq(request):
    return render(request, 'details/faq.html')
