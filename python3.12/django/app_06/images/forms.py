from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests
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

    def save(self, force_insert=False, force_update=False, commit=True):
        """Customisation a standart save method"""

        image = super().save(commit=False)
        url_image = self.cleaned_data["url"]
        name = slugify(image.title)
        extension = url_image.rsplit(".", 1)[1].lower()
        image_name = f"{name}.{extension}"
        response = requests.get(url_image)
        image.image.save(image_name, ContentFile(response.content), save=False)
        if commit:
            image.save()
        return image
