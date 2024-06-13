from django.db import IntegrityError
from rest_framework import serializers

from sdk_weather.models import Weather
from sdk_weather.services import get_weather


class WeatherListSerializer(serializers.ModelSerializer):
    """Main weather list serializer"""

    class Meta:
        model = Weather
        fields = '__all__'


class WeatherSerializer(serializers.ModelSerializer):
    """Weather serializer"""

    city = serializers.CharField(write_only=True)
    class Meta:
        model = Weather
        fields = ('city',)

    def to_representation(self, instance):
        return {
            "weather": {
                'main': instance.main,
                'description': instance.description,
            },
            "temperature": {
                'temp': instance.temp,
                'feels_like': instance.feels_like,
            },
            'visibility': instance.visibility,
            "wind": {
                'speed': instance.speed,
            },
            'datetime': instance.datetime,
            "sys": {
                'sunrise': instance.sunrise,
                'sunset': instance.sunset,
            },
            'timezone': instance.timezone,
            'name': instance.name,
        }

    def create(self, validated_data):
        """Standart function create"""
        
        city = validated_data.get('city')
        data = get_weather(city)
        try:

            if Weather.objects.count() >= 10:
                old_weather = Weather.objects.order_by('updated').first()
                old_weather.delete()
                print(f'Note {old_weather} deleted')

            weather, created = Weather.objects.update_or_create(
                name=data['name'],
                defaults=data
            )
        except IntegrityError:
            weather = Weather.objects.create(**data)
        return weather

