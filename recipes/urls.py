from django.urls import path
from .views import home, contact, about


urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('about/', about)
]
