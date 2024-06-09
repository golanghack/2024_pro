from django.urls import path
from service_2.views import process_data
from service_2.views import verify_signature

urlpatterns = [
    path('/process_data', process_data, name='data_processing'),
    path('/verify', verify_signature, name='verify'),
]    