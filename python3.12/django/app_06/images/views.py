from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from images.forms import ImageCreateForm
from images.models import Image


@login_required
def image_create(request):
    """View for creation a image link."""

    if request.method == "POST":
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
        new_image.user = request.user
        new_image.save()
        messages.success(request, "Image added")
        return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    template_name = "images/image/create.html"
    context = {
        "section": "images",
        "form": form,
    }
    return render(request, template_name, context)


def image_detail(request, id, slug):
    """View for detail info about image"""

    image = get_object_or_404(Image, id=id, slug=slug)
    template_name = "images/image/detail.html"
    context = {
        "section": "images",
        "image": image,
    }
    return render(request, template_name, context)
