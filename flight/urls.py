from django.urls import path
from .import views

urlpatterns = [
    path('flight_book',views.flight_book,name='flight_book'),
    path('<slug:c_slug>/',views.flight_book,name='Fly_cat'),
    path('flight_reservation',views.flight_reservation,name='flight_reservation'),
    path('flight_payment',views.flight_payment,name='flight_payment'),
    
    
]
