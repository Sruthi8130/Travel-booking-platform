from django.shortcuts import render,get_object_or_404
from django.urls import path
from .models import *


def cab_book(request,c_slug=None):
    c_page=None
    ca=None
    if c_slug!=None:
        c_page=get_object_or_404(Cab,slug=c_slug)
        ca=Cars.objects.filter(category=c_page)
    else:
        ca=Cars.objects.all().filter()
        
        
    ct=Cab.objects.all()
    return render(request,'cab_book.html',{'ca':ca,'ct':ct})

def cab_reservation(request):
    return render(request,'cab_reservation.html')

def cab_payment(request):
    return render(request,'cab_payment.html')

