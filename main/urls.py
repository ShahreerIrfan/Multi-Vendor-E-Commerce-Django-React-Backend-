from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('address',views.CustomerAddressViewset)

urlpatterns = [
   path('vendors/',views.VendorList.as_view(),name = 'vendor_list'),
   path('vendors/<int:pk>',views.VendorDetails.as_view(),name = 'vendor_details'),
   path('products/',views.ProductList.as_view(),name = 'products'),
   path('products/<int:pk>',views.ProductDetails.as_view(),name = 'vendor_details'),
   # Customers
   path('customers/',views.CustomerList.as_view(),name = 'customers_list'),
   path('customer/<int:pk>',views.CustomerDetails.as_view(),name = 'customer_details'),
   #Order
   path('orders/',views.OrderList.as_view(),name = 'orders'),
   path('order/<int:pk>',views.OrderDetails.as_view(),name = 'order_details'),
]

urlpatterns+=router.urls


# .