from django.urls import path 
from service_1.views import generate_data_and_save

urlpatterns = [
    path('data/', generate_data_and_save, name='data')
]