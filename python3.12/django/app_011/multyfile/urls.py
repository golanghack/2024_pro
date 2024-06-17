from django.urls import path
from multyfile.views import FileUploadAPIView

urlpatterns = [
    path('', FileUploadAPIView.as_view(), name='file_upload'),
]