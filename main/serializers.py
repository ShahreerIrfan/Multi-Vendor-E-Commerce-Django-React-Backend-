from rest_framework import serializers
from . import models

class SellerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    class Meta:
        model = models.Vendor
        fields = ['user','address']
