from django.urls import path
from django.contrib.auth import views as auth
from account.views import dashboard


urlpatterns = [
    path("login/", auth.LoginView.as_view(), name="login"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("", dashboard, name="dashboard"),
]
