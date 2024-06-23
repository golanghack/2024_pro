from django import forms
from matrix.models import Matrix


class MatrixConnectionForm(forms.Form):
    matrix = forms.ModelChoiceField(queryset=Matrix.objects.all(),
                                    widget=forms.HiddenInput)
