from django.shortcuts import render
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
import redis
from images.forms import ImageCreateForm
from images.models import Image
from actions.utils import create_action

# redis configurted connect
redis_client = redis.Redis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)


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
            create_action(request.user, "image", new_image)
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
    total_images_views = redis_client.incr(f"image:{image.id}:views")
    redis_client.zincrby("image_ranking", 1, image.id)
    template_name = "images/image/detail.html"
    context = {
        "section": "images",
        "image": image,
        "total_views": total_images_views,
    }
    return render(request, template_name, context)


@login_required
@require_POST
def image_like(request):
    """View image like for auth user"""

    image_id = request.POST.get("id")
    action = request.POST.get("action")
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == "like":
                image.users_like.add(request.user)
                create_action(request.user, "likes", image)
            else:
                image.users_like.remove(request.user)
            context = {
                "status": "ok",
            }
            return JsonResponse(context)
        except Image.DoesNotExist:
            pass
        context = {
            "status": "error",
        }
        return JsonResponse(context)


@login_required
def image_ranking(request):
    """Return rank for image"""

    image_ranking = redis_client.zrange("image_ranking", 0, -1, desc=True)[:10]
    image_ranking_ids = [int(id) for id in image_ranking]
    # get most
    most_viewed = list(Image.objects.filter(id__in=image_ranking_ids))
    most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))
    template_name = "images/image/rank.html"
    context = {
        "section": "images",
        "most_viewed": most_viewed,
    }
    return render(request, template_name, context)
