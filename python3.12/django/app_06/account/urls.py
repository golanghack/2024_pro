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
        auth.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # reset
    path('password-reset/', auth.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
