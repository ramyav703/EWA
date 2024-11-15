from rest_framework import serializers
from chairsapp.models import Order  # Import the Order model
from chairsapp.models import Product

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'  # Include all fields from the Order model

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'