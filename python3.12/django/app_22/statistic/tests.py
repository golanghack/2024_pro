import pytest
from rest_framework.test import APIClient
from .models import FoodItem

@pytest.mark.django_db
def test_food_item_creation():
    client = APIClient()
    response = client.post('/api/food/', {
        "user_id": "test_user",
        "food_item": {
            "fdc_id": "8888888888888",
            "description": "waffle, butter, frozen",
            "food_category": "66666",
            "nutrients": {
                "energy_value": 333.2,
                "fat_value": 8.6,
                "protein_value": 88.6,
                "carbohydrate_value": 88.8,
                "fuel_category": "Better",
            },
            "meal_time": "Breakfast",
            "fuel_category": "Good",
            "created_at": "2024-08-06",
            "meal_repeat": [
                {"id": 34, "data": "2024-08-05", "meal": 24}
            ]
        }
    })

    assert response.status_code == 201
    assert FoodItem.objects.count() == 1
    assert FoodItem.objects.first().description == "waffle, butter, frozen"

@pytest.mark.django_db
def test_statistic_retrieval(client):
    FoodItem.objects.create(
        user_id='test_user',
        fdc_id='8888888888888',
        description='protein bar',
        food_category='snack',
        energy_value=200.0,
        fat_value=5.0,
        protein_value=20.0,
        carbohydrate_value=25.0,
        meal_time='Snack',
        fuel_category='Good',
        created_at='2024-08-01',
        meal_repeat='[]'
    )

    response = client.get('/api/statistics/', {'period': 'month'})

    assert response.status_code == 200
    assert response.data['total_items'] == 1
    assert response.data['total_energy'] == 200.0