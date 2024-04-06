from django import forms


class LoginForm(forms.Form):
    """Class for login user/.
    
    Attributes:
            username: The string username.
            password: The string password of username, as a widget.
    """

    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)
