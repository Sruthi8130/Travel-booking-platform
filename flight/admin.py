from django.contrib import admin
from .models import Flight,Fly

class FlightAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class FlyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'flight_number', 'departure_city', 'arrival_city', 'departure_time', 'arrival_time', 'price')
    list_filter = ('name', 'departure_city', 'arrival_city')
    search_fields = ('name', 'departure_city')
    

admin.site.register(Flight, FlightAdmin)
admin.site.register(Fly, FlyAdmin)
