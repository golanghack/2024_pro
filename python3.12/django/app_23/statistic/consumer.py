import json
from kafka import KafkaConsumer
from django.utils import timezone
from statistic.models import FoodItem, MealTime

def consume_food_messages():
    consumer = KafkaConsumer(
        'food',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='food-consumer-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        data = message.value
        user_id = data.get('user_id')  
        food_item_data = data.get('food_item')
        portion_data = data.get('portion')
        meal_time = data.get('meal_time')
        date = data.get('created_at')  
        food_item = FoodItem(
            fdc_id=food_item_data['fdc_id'],
            description=food_item_data['description'],
            food_category=food_item_data['food_category'],
            energy_value=food_item_data['nutrients']['energy_value'],
            fat_value=food_item_data['nutrients']['fat_value'],
            protein_value=food_item_data['nutrients']['protein_value'],
            carbohydrate_value=food_item_data['nutrients']['carbohydrate_value'],
            fuel_category=food_item_data['nutrients']['fuel_category'],
            user_id=user_id,
            created_at=timezone.now()
        )
        food_item.save()

        meal_time_entry = MealTime(
            food_item=food_item,
            meal_time=meal_time,
            portion_size=portion_data['portion_size'],
            date=timezone.datetime.strptime(date, '%Y-%m-%d').date()    
            )
        meal_time_entry.save()
