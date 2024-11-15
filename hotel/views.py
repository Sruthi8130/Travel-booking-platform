from django.shortcuts import render,get_object_or_404
from django.urls import path
from .models import *

def hotel_book(request,c_slug=None):
    c_page=None
    h=None
    if c_slug!=None:
        c_page=get_object_or_404(hotels,slug=c_slug)
        h=list.objects.filter(category=c_page)
    else:
        h=list.objects.all().filter()
        
        
    ct=hotels.objects.all()
    return render(request,'hotel_book.html',{'h':h,'ct':ct})


def hotel_reservation(request):
    return render(request,'hotel_reservation.html')

def hotel_payment(request):
    return render(request,'hotel_payment.html')

def booking_success(request):
    return render(request,'booking_success.html')

def roomdetails(request,c_slug,room_slug):
    try:
        rm=list.objects.get(category__slug=c_slug,slug=room_slug)
    except Exception as r:
        raise r
    return render(request,'hotel_room.html',{'rm':rm})
