from django.contrib import admin
from . models import Vendor,ProductCategory,Product

# Register your models here.
admin.site.register(Vendor)
admin.site.register(ProductCategory)
admin.site.register(Product)

