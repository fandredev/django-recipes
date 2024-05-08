from django.http import Http404, HttpRequest
from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Recipe
from django.db.models import Q

from utils.pagination import make_pagination


def home(request: HttpRequest):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")

    page_object, pagination_range = make_pagination(
        request, recipes, quantity_per_page=6, quantity_pages=4
    )

    return render(
        request,
        "recipes/pages/home.html",
        context={"recipes": page_object, "pagination_range": pagination_range},
    )


def category(request: HttpRequest, category_id: int):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by("-id")
    )
    page_object, pagination_range = make_pagination(
        request, recipes, quantity_per_page=6, quantity_pages=4
    )

    return render(
        request,
        "recipes/pages/category.html",
        context={
            "recipes": page_object,
            "pagination_range": pagination_range,
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


def search(request: HttpRequest):
    search_term = request.GET.get("q", "").strip()

    if not search_term:
        raise Http404()

    """
        Isso é equivalente a:
        Buscar em Recipe, campos que tenham is_published = True e dentro dessa regra:

        buscar em Recipe o campo title que contenha search_term 
        OU 
        buscar em Recipe o campo description que contenha search_term

        o Q é um objeto que permite a criação de queries complexas
   """

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) | Q(description__icontains=search_term),
        ),
        is_published=True,
    ).order_by("-id")

    page_object, pagination_range = make_pagination(
        request, recipes, quantity_per_page=6, quantity_pages=4
    )

    return render(
        request,
        "recipes/pages/search.html",
        {
            "page_title": f'Search for "{search_term}"',
            "search_term": search_term,
            "recipes": page_object,
            "pagination_range": pagination_range,
            "additional_url_query": f"&q={search_term}",
        },
    )
