from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Recipe
from http import HTTPStatus

from ..serializers import RecipeSerializer


@api_view(http_method_names=["GET", "POST"])
def recipe_api_list(request):
    if request.method == "GET":
        recipes = Recipe.objects.get_published()[:10]  # type: ignore
        # Sempre que for retornar mais de um objeto, é necessário passar o many=True
        serializer = RecipeSerializer(instance=recipes, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        serializer = RecipeSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        # return Response(serializer.validated_data, status=HTTPStatus.CREATED) # isso é bom para ver as validações
        return Response(
            serializer.data, status=HTTPStatus.CREATED
        )  # isso é bom para ver as validações


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
