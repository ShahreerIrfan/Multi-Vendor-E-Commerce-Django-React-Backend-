from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions

# Create your views here.

class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permission_classes = [IsAuthenticated]


class VendorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailsSerializer
    # permission_classes = [IsAuthenticated]
