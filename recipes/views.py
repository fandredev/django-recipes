from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request: HttpRequest):
    return render(request, 'recipes/home.html')


def contact(request: HttpRequest):
    return HttpResponse('Contact')


def about(request: HttpRequest):
    return HttpResponse('about')
