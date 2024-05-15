from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Recipe

from ..serializers import RecipeSerializer


@api_view(["GET"])
def recipe_api_list(request):
    recipes = Recipe.objects.get_published()[:10]  # type: ignore
    # Sempre que for retornar mais de um objeto, é necessário passar o many=True
    serializer = RecipeSerializer(instance=recipes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def recipe_api_detail(request, pk: int):
    recipes = get_object_or_404(Recipe, pk=pk, is_published=True)

    serializer = RecipeSerializer(instance=recipes)
    return Response(serializer.data)

    # recipe = Recipe.objects.get_published().filter(pk=pk).first()  # type: ignore

    # if recipe:
    #     serializer = RecipeSerializer(instance=recipe)
    #     return Response(serializer.data)
    # else:
    #     return Response(
    #         {
    #             "detail": "eita",
    #         },
    #         status=HTTPStatus.IM_A_TEAPOT,
    #     )
