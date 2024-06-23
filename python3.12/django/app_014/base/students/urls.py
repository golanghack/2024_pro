from django.urls import path
from django.views.decorators.cache import cache_page
from students import views


urlpatterns = [
    path('register/',
         views.StudentRegistrationView.as_view(),
         name='student_registration'),
    path('my-matrix/',
         views.StudentMatrixView.as_view(),
         name='student_my_matrix'),
    path('matrix/',
         views.StudentMatrixListView.as_view(),
         name='student_matrix_list'),
    path('matrix/<pk>/',
         cache_page(60 * 15)(views.StudentMatrixDetailView.as_view()),
         name='student_matrix_detail'),
    path('matrix/<pk>/<matrix_id>/',
         cache_page(60 * 15)(views.StudentMatrixDetailView.as_view()),
         name='student_matrix_detail_block'),

]
