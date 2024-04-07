from django.urls import path
from django.contrib.auth import views as auth
from account.views import dashboard


urlpatterns = [
    # auth
    path("login/", auth.LoginView.as_view(), name="login"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    # main
    path("", dashboard, name="dashboard"),
    # change a pass/log
    path(
        "password-change/",
        auth.PasswordChangeDoneView.as_view(),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]
