from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from account.forms import LoginForm


def user_login(request):
    """Return user for this login."""

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Success")
                else:
                    return HttpResponse("Disabled")
            else:
                return HttpResponse("Invalid")
    else:
        form = LoginForm()
    temp = "account/login.html"
    context = {"form": form}
    return render(request, temp, context)
