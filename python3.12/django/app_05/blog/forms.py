from django import forms
from blog.models import Comment


class EmailPostForm(forms.Form):
    """Email form for sending a post in email
    
    Attributes:
            name: The string for name a user sent email.
            email: The email for user.
            to: The email for to email.
            comments: The string(default len <= 1000 symbols) for email.
            """

    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(max_length=1000, required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """Dinamic formation for form a comment."""

    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
