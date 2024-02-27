from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('vendors/',views.VendorList.as_view(),name = 'vendor_list')
]