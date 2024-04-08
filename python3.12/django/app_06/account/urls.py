from django.urls import path, include
from account.views import dashboard
from account.views import register
from account.views import edit


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("edit/", edit, name="edit"),
]
