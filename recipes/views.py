from django.http import HttpRequest
from django.shortcuts import render

from utils.recipes.factory import make_recipe


def home(request: HttpRequest):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe for _ in range(10)]
    })


def recipe(request: HttpRequest, id: int):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
        'id': id
    })
