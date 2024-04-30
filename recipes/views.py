from django.http import HttpRequest
from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Recipe


def home(request: HttpRequest):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": recipes,
        },
    )


def category(request: HttpRequest, category_id: int):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by("-id")
    )

    return render(
        request,
        "recipes/pages/category.html",
        context={
            "recipes": recipes,
            "title": f"${recipes[0].category.name} - Category|",  # type: ignore
        },
    )


def recipe(request: HttpRequest, id: str):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={
            "recipe": recipe,
            "is_detail_page": True,
        },
    )
