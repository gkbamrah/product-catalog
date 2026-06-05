from django.db import models
from django.utils import timezone
import datetime

class Product(models.Model):
    name = models.CharField(max_length=200)
    post_date = models.DateTimeField("date posted")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.product_name
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name