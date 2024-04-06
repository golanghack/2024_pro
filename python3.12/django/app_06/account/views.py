from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    """Full dashboard after logged"""

    template_name = "account/dashboard.html"
    context = {"section": "dashboard"}
    return render(request, template_name, context)
