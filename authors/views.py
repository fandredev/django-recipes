from django.http import HttpRequest
from django.shortcuts import render

def register_view(request: HttpRequest):
    return render(request, 'authors/pages/register_view.html')