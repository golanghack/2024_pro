from django.db import models
from django.utils.translation import gettext_lazy as _


class FoodItem(models.Model):
    user_id = models.CharField(max_length=100, db_index=True, unique=True, verbose_name=_('user id'))
    fdc_id = models.CharField(max_length=100, db_index=True, unique=True, verbose_name=_('fdc id'))
    description = models.CharField(max_length=300, verbose_name=_('description'))
    food_category = models.CharField(max_length=80, verbose_name=_('food_category'))
    energy_value = models.FloatField(blank=True, null=False, verbose_name=_('energy value'))
    fat_value = models.FloatField(blank=True, null=False, verbose_name=_('fat value'))
    protein_value = models.FloatField(blank=True, null=False, verbose_name=_('protein_value'))
    carbohydrate_value = models.FloatField(blank=True, null=False, verbose_name=_('carbohydrate value'))
    meal_time = models.DateTimeField(verbose_name=_('added meal time'))
    fuel_category = models.CharField(max_length=20, null=False, verbose_name=_('category fuel'))
    created_at = models.DateField()
    meal_repeat = models.JSONField()

    def __str__(self):
        return self.description