from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request: HttpRequest):
    return HttpResponse('Home 1')


def contact(request: HttpRequest):
    return HttpResponse('Contact')


def about(request: HttpRequest):
    return HttpResponse('about')
