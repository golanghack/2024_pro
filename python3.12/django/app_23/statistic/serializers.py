from rest_framework import serializers
from .models import MealTime, FoodItem

class MealTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealTime
        fields = '__all__'
        
        
class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'        