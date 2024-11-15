# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify
from services.models import*
from django.urls import reverse


# Create your models here.


class Cab(models.Model):
    name = models.TextField(max_length=99,null=True)
    slug = models.SlugField(max_length=99,null=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('Cars_cat',args=[self.slug])

class Cars(models.Model):
    name = models.TextField(max_length=99,null=True)
    slug = models.SlugField(max_length=99,null=True)
    cab_number=models.TextField(max_length=999,null=True)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    travel_date = models.DateField(null=True)
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img  = models.CharField(max_length=9999,null=True)
    category = models.ForeignKey(Cab,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name


