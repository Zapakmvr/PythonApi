from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('Name', 'Description', 'Code')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('Code', 'ProductCode')