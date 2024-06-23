from django.urls import path, include
from rest_framework import routers
from matrix.api import views


app_name = 'blocks'


router = routers.DefaultRouter()
router.register('blocks', views.MatrixViewSet)


urlpatterns = [
    path('subjects/',
         views.SubjectListView.as_view(),
         name='subject_list'),
    path('subjects/<pk>/',
         views.SubjectDetailView.as_view(),
         name='subject_detail'),

     path('', include(router.urls)),
]
