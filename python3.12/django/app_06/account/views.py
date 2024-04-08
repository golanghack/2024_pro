from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from account.forms import LoginForm, UserRegistrationForm
from account.models import Profile


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
