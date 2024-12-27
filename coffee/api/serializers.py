from rest_framework import serializers
from .models import CoffeeType, Ingredient, Order, MaintenanceTask

class CoffeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeType
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class MaintenanceTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceTask
        fields = '__all__'
