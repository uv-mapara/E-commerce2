from tkinter import CASCADE
from enum import unique
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import datetime
import uuid

# Create your models here.

class Signup(models.Model):
    firstname=models.CharField( max_length=50)
    lastname=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField(default='')
    password=models.CharField(max_length=50)    

    def __str__(self):
        return self.firstname

class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Subcategories(models.Model):
    subcat = models.ForeignKey(Categories,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):   
    CONDITION=(('New','New'),('Old','Old'))
    STOCK=(('IN STOCK','IN STOCK'),('OUT OF STOCK','OUT OF STOCK'))
    STATUS=(('PUBLISH','PUBLISH'),('DRAFT','DRAFT'))

    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    subcategories=models.ForeignKey(Subcategories,on_delete=models.CASCADE)  
    unique_id=models.CharField(unique=True,max_length=200,null=True,blank=True)     
    name=models.CharField(max_length=200)
    price = models.FloatField()         
    total_stock=models.PositiveIntegerField()
    image=models.ImageField(upload_to='product-img/')    
    description=RichTextField(null=True)
    created_date=models.DateTimeField(default=timezone.now)   
    S = models.PositiveIntegerField()
    M = models.PositiveIntegerField()
    L = models.PositiveIntegerField()
    
    condition=models.CharField(choices=CONDITION,max_length=100)
    stock=models.CharField(choices=STOCK,max_length=200)
    status=models.CharField(choices=STATUS,max_length=200)
    views = models.PositiveIntegerField(default=0)
    #filter_price=models.ForeignKey(Filter_Price,on_delete=models.CASCADE)    

    def save(self, *args , **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args,**kwargs)

class Mycart(models.Model):
    user=models.ForeignKey(Signup,null=True,blank=True, on_delete=models.CASCADE)    
    product=models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity=models.PositiveIntegerField()   
    status=models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    update_on= models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):        
        return self.user.firstname
