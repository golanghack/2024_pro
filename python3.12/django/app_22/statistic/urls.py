from django.urls import path
from .views import FoodMessageHandler, StatisticsView

urlpatterns = [
    path('food/', FoodMessageHandler.as_view(), name='food-message'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]