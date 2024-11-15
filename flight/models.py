from django.db import models
from django.template.defaultfilters import slugify
from services.models import*
from django.urls import reverse


# Create your models here.


class Flight(models.Model):
    name = models.TextField(max_length=99,null=True)
    slug = models.SlugField(max_length=99,null=True)


    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('Fly_cat',args=[self.slug])

class Fly(models.Model):
    name = models.TextField(max_length=99,null=True)
    slug = models.SlugField(max_length=99,null=True)
    flight_number = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    travel_date = models.DateField(null=True)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Flight,on_delete=models.CASCADE,null=True)
    

    def str (self):
        return self.name

