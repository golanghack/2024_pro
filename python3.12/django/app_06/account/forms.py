from django import forms
from django.contrib.auth.models import User
from account.models import Profile


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

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Password dont match")
        return cd["password2"]
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use')
        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "date_of_birth",
            "photo",
        ]
