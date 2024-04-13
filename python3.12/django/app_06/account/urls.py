from django.urls import path, include
from account.views import dashboard
from account.views import register
from account.views import edit
from account.views import user_list
from account.views import user_detail
from account.views import user_follow


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("edit/", edit, name="edit"),
    path("users/", user_list, name="user_list"),
     path('users/follow/', user_follow, name='user_follow'),
    path("users/<username>/", user_detail, name="user_detail"),
]
