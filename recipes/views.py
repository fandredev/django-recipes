from django.http import Http404, HttpRequest
from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Recipe
from django.db.models import Q

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

def search(request: HttpRequest):
   search_term = request.GET.get('q', '').strip()

   if not search_term:
       raise Http404()
   
   recipes = Recipe.objects.filter(
       Q(
        Q(title__icontains=search_term) | Q(description__icontains=search_term),  
       ),
       is_published=True
   ).order_by('-id')


   """
        Isso é equivalente a:
        Buscar em Recipe, campos que tenham is_published = True e dentro dessa regra:

        buscar em Recipe o campo title que contenha search_term 
        OU 
        buscar em Recipe o campo description que contenha search_term

        o Q é um objeto que permite a criação de queries complexas
   """


   return render(request, "recipes/pages/search.html", {
       'page_title': f'Search for "{search_term}"',
       'search_term': search_term,
       'recipes': recipes,
   })