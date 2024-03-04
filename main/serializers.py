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


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        depth = 1 

    def __init__(self, *args, **kwargs):
        super(ProductListSerializer, self).__init__(*args, **kwargs)



class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        depth = 1 

    def __init__(self, *args, **kwargs):
        super(ProductDetailsSerializer, self).__init__(*args, **kwargs)


#Customer serializer  
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'
        depth = 1

        def __init__(self,*args,**kwargs):
            super(CustomerSerializer,self).__init__(*args,**kwargs)
            self.Meta.depth = 1

class CustomerDetailsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.Customer
        fields = '__all__'
        depth = 1 

    def __init__(self, *args, **kwargs):
        super(CustomerDetailsSerializer, self).__init__(*args, **kwargs)


# Orders Serializers part
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'
        depth = 1

class OrderDetailsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.OrderItems
        fields = '__all__'
        depth = 1 

    def __init__(self, *args, **kwargs):
        super(OrderDetailsSerializer, self).__init__(*args, **kwargs)



class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        fields = '__all__'

class CustomerAddressSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.CustomerAddress
        fields = '__all__'
        depth = 1 

    def __init__(self, *args, **kwargs):
        super(CustomerAddressSerializer, self).__init__(*args, **kwargs)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = '__all__'
        depth = 1

        def __init__(self,*args,**kwargs):
            super(CategorySerializer,self).__init__(*args,**kwargs)
            self.Meta.depth = 1

class CategoryDetailsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.ProductCategory
        fields = '__all__'
        depth = 1 