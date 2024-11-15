from django.contrib import admin
from .models import hotels,list

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class ListAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','check_date', 'check_time')
    list_filter = ('place', 'check_date')
    search_fields = ('place', 'price')

admin.site.register(hotels,HotelAdmin)
admin.site.register(list,ListAdmin)