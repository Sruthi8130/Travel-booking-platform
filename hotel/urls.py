from django.urls import path
from .import views

urlpatterns = [

    path('hotel_book',views.hotel_book,name='hotel_book'),
    path('<slug:c_slug>/',views.hotel_book,name='list_cat'),
    path('hotel_reservation',views.hotel_reservation,name='hotel_reservation'),
    path('hotel_payment',views.hotel_payment,name='hotel_payment'),
    path('booking_success',views.booking_success,name='booking_success'),
    path('<slug:c_slug>/<slug:room_slug>',views.roomdetails,name='details'),
    
] 
