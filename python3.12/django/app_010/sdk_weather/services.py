from datetime import datetime

import requests
from django.conf import settings
from django.utils import timezone
from rest_framework import serializers


def get_weather(city, api_key_1=settings.WEATHER_API_KEY_1, api_key_2=settings.WEATHER_API_KEY_2):
    """Get weather data from openweather api"""

    # condition for api
    if api_key_1 == api_key_2:
        raise ValueError('Yuor api key the same')

    # url for openweather
    url = "https://api.openweathermap.org/data/2.5/weather"
    # parameters for connection
    params = {
        "q": {city},
        "units": "imperial",
        "appid": {api_key_1}
    }
    # get a data from api
    data = requests.get(url, params=params).json()
    # condition for weathewr data for 404 err
    if data.get('cod') == '404':
        raise serializers.ValidationError("City not found", code=404)
    # unit info
    info = {
        "main": data['weather'][0]['main'],
        "description": data['weather'][0]['description'],
        "temp": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "visibility": data['visibility'],
        "speed": data['wind']['speed'],
        "datetime": timezone.make_aware(datetime.utcfromtimestamp(data['dt']).replace(microsecond=0)),
        "sunrise": timezone.make_aware(datetime.utcfromtimestamp(data['sys']['sunrise']).replace(microsecond=0)),
        "sunset": timezone.make_aware(datetime.utcfromtimestamp(data['sys']['sunset']).replace(microsecond=0)),
        "timezone": data['timezone'],
        "name": data['name'],
    }

    return info
