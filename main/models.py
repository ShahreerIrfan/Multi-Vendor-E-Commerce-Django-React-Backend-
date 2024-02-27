from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Vendor model
class Vendor(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    address = models.TextField(null = True)

    def __str__(self) -> str:
        return self.user.username

# Product Category Moder
class ProductCategory(models.Model):
    title = models.CharField(max_length = 100)
    details = models.TextField(null = True)

    def __str__(self) -> str:
        return self.title
    
# Product model
    
class Product(models.Model):
    category = models.ForeignKey(ProductCategory,on_delete = models.SET_NULL,null = True)
    vendor = models.ForeignKey(Vendor,on_delete = models.SET_NULL,null = True)
    title = models.CharField(max_length = 100)
    details = models.TextField(null = True)
    price  =  models.FloatField()
    def __str__(self) -> str:
        return self.title