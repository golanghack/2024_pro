from django.urls import path
from pages.views import home_page

urlpatterns = [
    path('', home_page, name='home'),
]
