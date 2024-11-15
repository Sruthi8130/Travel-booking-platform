from django.db import models
from django.template.defaultfilters import slugify
from services.models import*
from django.urls import reverse


# Create your models here.


class hotels(models.Model):
    name = models.TextField(max_length=99,null=True)
    slug = models.SlugField(max_length=99,null=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('list_cat',args=[self.slug])

class list(models.Model):
    name = models.TextField(max_length=99,null=True)
    slug = models.SlugField(max_length=99,null=True)
    place= models.CharField(max_length=100)
    check_date = models.DateField(null=True)
    check_time = models.TimeField()
    hotel_img = models.CharField(max_length=9999)
    hotel_desc = models.TextField(max_length=999,null=True)
    first_room_img = models.CharField(max_length=9999,null=True)
    second_room_img = models.CharField(max_length=9999,null=True)
    third_room_img = models.CharField(max_length=9999,null=True)
    first_room_type = models.TextField(max_length=99,null=True)
    second_room_type = models.TextField(max_length=99,null=True)
    third_room_type = models.TextField(max_length=99,null=True)
    first_desc = models.TextField(max_length=9999,null=True)
    second_desc = models.TextField(max_length=9999,null=True)
    third_desc = models.TextField(max_length=9999,null=True)
    first_room_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    second_room_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    third_room_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    first_img = models.CharField(max_length=999,null=True)
    second_img = models.CharField(max_length=999,null=True)
    third_img = models.CharField(max_length=999,null=True)
    fourth_img = models.CharField(max_length=999,null=True)
    fifth_img = models.CharField(max_length=999,null=True)
    sixth_img = models.CharField(max_length=999,null=True)
    category = models.ForeignKey(hotels,on_delete=models.CASCADE,null=True)

    def __str__(self):
         return self.name
    
    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])