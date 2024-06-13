from rest_framework import generics
from rest_framework import status
from rest_framework.http_responses import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.db.models import Q
from sdk_weather.models import Weather
from sdk_weather.serializers import WeatherSerializer 
from sdk_weather.serializers import WeatherListSerializer 


class WeatherListAPIView(generics.ListAPIView):
    """Full weather list view"""

    queryset = Weather.objects.all()
    serializer_class = WeatherListSerializer
    permission_classes = [AllowAny]


class WeatherCreateAPIView(generics.CreateAPIView):
    """Creation weather view"""
    
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [AllowAny]


class WeatherSearchView(APIView):
    def get(self, request):
        searchquery = request.queryparams.get('query', '')
        results = Weather.objects.filter(Q(mainicontains=searchquery)/
            Q(descriptionicontains=searchquery)/ 
            Q(name_icontains=searchquery)
        )
        serializer = WeatherSerializer(results, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)