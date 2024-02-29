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
    category = models.ForeignKey(ProductCategory,on_delete = models.SET_NULL,null = True,related_name = 'category_product')
    vendor = models.ForeignKey(Vendor,on_delete = models.SET_NULL,null = True)
    title = models.CharField(max_length = 100)
    details = models.TextField(null = True)
    price  =  models.FloatField()
    def __str__(self) -> str:
        return self.title
    
#Customer  Model

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    mobile = models.CharField(max_length =20)

    def __str__(self) -> str:
        return f"{self.user.first_name}  {self.user.last_name}"
    
#Order  model

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    order_time = models.DateTimeField(auto_now_add = True)

class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete = models.CASCADE,related_name = 'order_items')
    product = models.ForeignKey(Product,on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.product.title

# Customer address model

class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE,related_name = 'customerAddress')
    address = models.TextField()
    default_address = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.address