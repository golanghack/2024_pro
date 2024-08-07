
from django.db import models

class FoodItem(models.Model):
    fdc_id = models.IntegerField()
    description = models.CharField(max_length=255)
    food_category = models.IntegerField()
    energy_value = models.FloatField()
    fat_value = models.FloatField()
    protein_value = models.FloatField()
    carbohydrate_value = models.FloatField()
    fuel_category = models.CharField(max_length=50)
    user_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class MealTime(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    meal_time = models.CharField(max_length=50)
    portion_size = models.FloatField()
    date = models.DateField()
