from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """Class for login user/.

    Attributes:
            username: The string username.
            password: The string password of username, as a widget.
    """

    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """User registration form

    Attributes:
            password: string a password.
            password2: string a password.
            models: default model for user.
            fields: fields for read.
    """

    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "email",
        ]
