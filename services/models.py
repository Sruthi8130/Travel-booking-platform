from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class categ(models.Model):
    name = models.CharField(max_length=500,unique=True)
    slug = models.SlugField(max_length=500,unique=True)

    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('ser_cat',args=[self.slug])

class services(models.Model):
    name = models.CharField(max_length=999,unique=True)
    slug = models.SlugField(max_length=999,unique=True)
    img = models.CharField(max_length=9999,unique=True)
    price = models.IntegerField()
    desc = models.TextField()
    available = models.BooleanField()
    category = models.ForeignKey(categ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

