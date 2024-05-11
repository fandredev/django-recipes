from django.http import Http404
from .models import Recipe
from django.db.models import Q

from utils.pagination import make_pagination
import os
from django.views.generic import (
    ListView,
    DetailView,
)

PER_PAGE = int(os.environ.get("PER_PAGE", 6))


class RecipeListViewBase(ListView):
    model = Recipe
    context_object_name = "recipes"
    ordering = ["-id"]
    template_name = "recipes/pages/home.html"

    def get_queryset(self, *args, **kwargs):
        query_set = super().get_queryset(*args, **kwargs)
        query_set = query_set.filter(
            is_published=True,
        )
        return query_set

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        page_obj, pagination_range = make_pagination(
            self.request,
            ctx.get("recipes"),
            PER_PAGE,
        )
        ctx.update(
            {
                "recipes": page_obj,
                "pagination_range": pagination_range,
            }
        )
        return ctx


class RecipeListViewHome(RecipeListViewBase):
    template_name = "recipes/pages/home.html"


class RecipeListViewCategory(RecipeListViewBase):
    template_name = "recipes/pages/category.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({"title": f'{ctx.get("recipes")[0].category.name} - Category | '})  # type: ignore

        return ctx

    def get_queryset(self, *args, **kwargs):
        query_set = super().get_queryset(*args, **kwargs)
        query_set = query_set.filter(category__id=self.kwargs.get("category_id"))

        if not query_set.exists():
            raise Http404()

        return query_set


class RecipeListViewSearch(RecipeListViewBase):
    template_name = "recipes/pages/search.html"

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get("q", "").strip()
        query_set = super().get_queryset(*args, **kwargs)

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
        query_set = query_set.filter(
            Q(
                Q(title__icontains=search_term) | Q(description__icontains=search_term),
            ),
            is_published=True,
        )

        return query_set

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get("q", "").strip()
        page_obj, pagination_range = make_pagination(
            self.request,
            ctx.get("recipes"),
            PER_PAGE,
        )
        ctx.update(
            {
                "page_title": f'Search for "{search_term}"',
                "search_term": search_term,
                "additional_url_query": f"&q={search_term}",
                "recipes": page_obj,
                "pagination_range": pagination_range,
            }
        )
        return ctx


class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = "recipe"
    template_name = "recipes/pages/recipe-view.html"

    def get_queryset(self, *args, **kwargs):
        query_set = super().get_queryset(*args, **kwargs)
        query_set = query_set.filter(
            is_published=True,
        )
        return query_set

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update(
            {
                "is_detail_page": True,
            }
        )

        return ctx
