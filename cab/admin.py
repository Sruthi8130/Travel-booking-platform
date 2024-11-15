from django.contrib import admin
from .models import Cab,Cars

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class CabAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name','departure_city', 'arrival_city','time', 'price')
    list_filter = ('name','departure_city', 'arrival_city')
    search_fields = ('name', 'cab_number')

admin.site.register(Cab, CarAdmin)
admin.site.register(Cars,CabAdmin)