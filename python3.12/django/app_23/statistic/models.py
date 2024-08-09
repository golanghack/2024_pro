
from django.db import models
from django.http import request
from django.contrib.auth.models import User
from auth import extract_user_id_from_token

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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.user.username
    