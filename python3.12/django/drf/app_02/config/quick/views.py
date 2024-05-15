from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from config.quick.serializers import GroupSerializer, UserSerializer 

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group
    """
    
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    