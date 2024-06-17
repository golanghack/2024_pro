from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from multyfile.models import FileUpload
from multyfile.serializer import FileUploadSerializer
from multyfile.serializer import FileUploadDisplaySerializer

class FileUploadAPIView(generics.ListCreateAPIView):
    """FileUpload API"""
    
    permission_classes = [AllowAny, ]
    serializer_class = FileUploadDisplaySerializer
    
    def post(self, request, format=None):
        serializer = FileUploadDisplaySerializer(data=request.data)
        if serializer.is_valid():
            qs = serializer.data
            message = {'detail': qs, 'status': True}
            return Response(message, status=status.HTTP_201_CREATED)
        else:
            data = {'detail': serializer.errors, 'status': False}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        return FileUpload.objects.all()         
