from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(request, 'home.html')

def about(request):
    return HttpResponse('About')

    
    