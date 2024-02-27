from rest_framework import serializers
from . import models

class VendorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    class Meta:
        model = models.Vendor
        fields = ['id','user','address']

        def __init__(self,*args,**kwargs):
            super(VendorSerializer,self).__init__(*args,**kwargs)
            self.Meta.depth = 1

class VendorDetailsSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)  
    class Meta:
        model = models.Vendor
        fields = ['id', 'user', 'address']
        depth = 1 

    def __init__(self, *args, **kwargs):
        super(VendorDetailsSerializer, self).__init__(*args, **kwargs)
