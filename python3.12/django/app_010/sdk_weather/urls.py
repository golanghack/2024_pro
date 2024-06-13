from django.urls import path

from sdk_weather.apps import SdkWeatherConfig
from sdk_weather.views import WeatherCreateAPIView
from sdk_weather.views import WeatherListAPIView
from sdk_weather.views import WeatherSearchView

app_name = SdkWeatherConfig.name

urlpatterns = [
    path('api/weather/all/', WeatherListAPIView.as_view(), name='weather-list'),
    path('api/weather/', WeatherCreateAPIView.as_view(), name='weather-create'),
    path('api/search/', WeatherSearchView.as_view(), name='search'),
]
