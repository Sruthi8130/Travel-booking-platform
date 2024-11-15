from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def mainpage(request):
    return render(request,'mainpage.html')
    
def home(request,c_slug=None):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

def package(request,c_slug=None):
    c_page=None
    s=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        s=services.objects.filter(category=c_page,available=True)
    else:
        s=services.objects.all().filter(available=True)
        
        
    ct=categ.objects.all()
    return render(request,'package.html',{'s':s,'ct':ct})