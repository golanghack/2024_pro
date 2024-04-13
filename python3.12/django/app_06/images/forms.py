from django import forms
from images.models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [
            "title",
            "url",
            "description",
        ]
        widgets = {
            "url": forms.HiddenInput,
        }

    def clean_url(self):
        """Validation for field an url"""

        url = self.cleaned_data["url"]
        valid_extensions = ["jpg", "jpeg", "png"]
        extension = url.rsplit(".", 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError("The URL does not valid image extensions")
        return url
