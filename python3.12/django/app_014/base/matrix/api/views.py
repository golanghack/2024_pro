from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from matrix.models import Subject, Matrix
from matrix.api.serializers import SubjectSerializer, MatrixSerializer
from matrix.api.permissions import IsEnrolled
from matrix.api.serializers import MatrixWithContentsSerializer



class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



class MatrixViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Matrix.objects.all()
    serializer_class = MatrixSerializer

    @action(detail=True,
            methods=['post'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        matrix = self.get_object()
        matrix.students.add(request.user)
        return Response({'connect': True})

    @action(detail=True,
            methods=['get'],
            serializer_class=MatrixWithContentsSerializer,
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
