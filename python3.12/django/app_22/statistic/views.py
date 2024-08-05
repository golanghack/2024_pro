from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodItem
from .kafka import KafkaHandler
from django.utils import timezone
from datetime import timedelta
import pandas as pd

kafka_handler = KafkaHandler()

class FoodMessageHandler(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_kafka_consumer()

    def start_kafka_consumer(self):
        for message in kafka_handler.consume():
            self.process_message(message)

    def process_message(self, data):
        food_item = FoodItem(
            user_id=data['user_id'],
            fdc_id=data['food_item']['fdc_id'],
            description=data['food_item']['description'],
            food_category=data['food_item']['food_category'],
            energy_value=data['food_item']['nutrients']['energy_value'],
            fat_value=data['food_item']['nutrients']['fat_value'],
            protein_value=data['food_item']['nutrients']['protein_value'],
            carbohydrate_value=data['food_item']['nutrients']['carbohydrate_value'],
            meal_time=data['food_item']['meal_time'],
            fuel_category=data['food_item']['fuel_category'],
            created_at=data['food_item']['created_at'],
            meal_repeat=data['food_item']['meal_repeat'],
        )
        food_item.save()
        
        # Отправка статуса в Kafka
        kafka_handler.produce('get_food', {'status': 'Message received and stored successfully.'})

class StatisticsView(APIView):
    def get(self, request):
        period = request.query_params.get('period', 'day')
        end_date = timezone.now()
        start_date = self.calculate_start_date(period, end_date)

        food_items = FoodItem.objects.filter(created_at__range=[start_date, end_date])

        # Рассчет статистики
        statistics = self.calculate_statistics(food_items)

        return Response(statistics, status=status.HTTP_200_OK)

    def calculate_start_date(self, period, end_date):
        if period == 'day':
            return end_date - timedelta(days=1)
        elif period == 'week':
            return end_date - timedelta(weeks=1)
        elif period == 'month':
            return end_date - timedelta(weeks=4)
        else:
            return end_date

    def calculate_statistics(self, food_items):
        if not food_items:
            return {}

        df = pd.DataFrame(list(food_items.values()))
        summary = {
            'total_items': len(df),
            'total_energy': df['energy_value'].sum(),
            'total_fat': df['fat_value'].sum(),
            'total_protein': df['protein_value'].sum(),
            'total_carbohydrates': df['carbohydrate_value'].sum(),
        }
        return summary