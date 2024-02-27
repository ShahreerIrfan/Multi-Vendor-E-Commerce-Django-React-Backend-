from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.

class VendorList(generics.ListAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.SellerSerializer
