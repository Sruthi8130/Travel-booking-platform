from django.urls import path
from .import views

urlpatterns = [
    path('cab_book',views.cab_book,name='cab_book'),
    path('<slug:c_slug>/',views.cab_book,name='Cars_cat'),
    path('cab_reservation',views.cab_reservation,name='cab_reservation'),
    path('cab_payment',views.cab_payment,name='cab_payment')
    
    
]