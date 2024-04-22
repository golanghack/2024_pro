from django.urls import path
from images.views import image_create
from images.views import image_detail
from images.views import image_like
from images.views import image_ranking

app_name = "images"

urlpatterns = [
    path("create/", image_create, name="create"),
    path("detail/<int:id>/<slug:slug>/", image_detail, name="detail"),
    path("like/", image_like, name="like"),
    path('rank/', image_ranking, name='rank'),
]
