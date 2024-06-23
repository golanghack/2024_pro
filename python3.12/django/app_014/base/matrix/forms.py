from django import forms
from django.forms.models import inlineformset_factory
from matrix.models import Matrix, Block

BlockFormSet = inlineformset_factory(Matrix,
                                      Block,
                                      fields=['title',
                                              'description'],
                                      extra=2,
                                      can_delete=True)
