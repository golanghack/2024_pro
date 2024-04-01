from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(max_length=1000, required=False, widget=forms.Textarea)
    