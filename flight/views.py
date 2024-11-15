from django.shortcuts import render,get_object_or_404
from django.urls import path
from .models import *


def flight_book(request,c_slug=None):
    c_page=None
    f=None
    if c_slug!=None:
        c_page=get_object_or_404(Flight,slug=c_slug)
        f=Fly.objects.filter(category=c_page)
    else:
        f=Fly.objects.all().filter()
        
        
    ct=Flight.objects.all()
    return render(request,'flight_book.html',{'f':f,'ct':ct})
    
def flight_reservation(request):
    return render(request,'flight_reservation.html')

def flight_payment(request):
    return render(request,'flight_payment.html')

