from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path

schema_view = get_schema_view(openapi.Info(
title="Food Service API",
           default_version='v1',
           description="API for managing food items and statistics",
           terms_of_service="https://www.google.com/policies/terms/",
           contact=openapi.Contact(email="contact@food.local"),
           license=openapi.License(name="BSD License"),
       ),
       public=True,
   )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('statistic.urls')),
]
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
