from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from django.db import models 
from django.utils import timezone
from statistic.models import FoodItem, MealTime
from statistic.serializers import FoodItemSerializer
from datetime import timedelta

class StatisticsViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    def get_daily_statistics(self, request):
        user_id = request.user.id  
        today = timezone.now().date()
        daily_stats = MealTime.objects.filter(date=today, food_item__user_id=user_id).aggregate(
            total_meals=models.Count('id'),
            total_energy=models.Sum('food_item__energy_value'),
            total_fat=models.Sum('food_item__fat_value'),
            total_protein=models.Sum('food_item__protein_value'),
            total_carbohydrates=models.Sum('food_item__carbohydrate_value')
        )
        return Response(daily_stats)

    def get_weekly_statistics(self, request):
        user_id = request.user.id
        start_of_week = timezone.now().date() - timedelta(days=timezone.now().weekday())
        weekly_stats = MealTime.objects.filter(date__gte=start_of_week, food_item__user_id=user_id).aggregate(
            total_meals=models.Count('id'),
            total_energy=models.Sum('food_item__energy_value'),
            total_fat=models.Sum('food_item__fat_value'),
            total_protein=models.Sum('food_item__protein_value'),
            total_carbohydrates=models.Sum('food_item__carbohydrate_value')
        )
        return Response(weekly_stats)

    def get_monthly_statistics(self, request):
        user_id = request.user.id
        start_of_month = timezone.now().date().replace(day=1)
        monthly_stats = MealTime.objects.filter(date__gte=start_of_month, food_item__user_id=user_id).aggregate(
            total_meals=models.Count('id'),
            total_energy=models.Sum('food_item__energy_value'),
            total_fat=models.Sum('food_item__fat_value'),
            total_protein=models.Sum('food_item__protein_value'),
            total_carbohydrates=models.Sum('food_item__carbohydrate_value')
        )
        return Response(monthly_stats)

class FoodItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return self.queryset.filter(user_id=user_id)