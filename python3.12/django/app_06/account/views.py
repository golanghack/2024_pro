from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from account.forms import UserRegistrationForm
from account.forms import UserEditForm
from account.forms import ProfileEditForm
from account.models import Profile
from account.models import Contact
from actions.utils import create_action


@login_required
def dashboard(request):
    """Full dashboard after logged"""

    template_name = "account/dashboard.html"
    context = {"section": "dashboard"}
    return render(request, template_name, context)


def register(request):
    """User registration view"""

    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create new
            new_user = user_form.save(commit=False)
            # set password
            new_user.set_password(user_form.cleaned_data["password"])
            # save
            new_user.save()
            Profile.objects.create(user=new_user)
            create_action(new_user, "created an account")
            template_name = "account/register_done.html"
            context = {
                "new_user": new_user,
            }
            return render(request, template_name, context)
    else:
        user_form = UserRegistrationForm()
    template_name = "account/register.html"
    context = {
        "user_form": user_form,
    }
    return render(request, template_name, context)


@login_required
def edit(request):
    """Editing a profile of user."""

    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated", "success")
        else:
            messages.error(request, "Error with updated")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    template_name = "account/edit.html"
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, template_name, context)


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    template_name = "account/user/list.html"
    context = {
        "section": "people",
        "users": users,
    }
    return render(request, template_name, context)


@login_required
def user_detail(request, username):
    user = get_list_or_404(User, username=username, is_active=True)
    template_name = "account/user/detail.html"
    context = {
        "section": "people",
        "user": user,
    }
    return render(request, template_name, context)


@login_required
@require_POST
def user_follow(request):
    user_id = request.POST.get("id")
    action = request.POST.get("action")
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == "follow":
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            ok_context = {
                "status": "ok",
            }
            return JsonResponse(ok_context)
        except User.DoesNotExist:
            err_user_context = {
                "status": "error",
            }
            return JsonResponse(err_user_context)
    err_context = {
        "status": "error",
    }
    return JsonResponse(err_context)
