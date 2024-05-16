from ..models import Recipe

from ..serializers import RecipeSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework import request, response
from rest_framework.viewsets import ModelViewSet


class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 2


class RecipeAPIV2ViewSet(ModelViewSet):
    queryset = Recipe.objects.get_published()  # type: ignore
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination

    def get_queryset(self):
        qs = super().get_queryset()
        print("Paramêtros", self.kwargs)

        category_id = self.request.query_params.get("category_id", "")  # type: ignore

        if category_id != "" and category_id.isnumeric():
            qs = qs.filter(category_id=category_id)

        return qs

    def partial_update(self, request: request.Request, *args, **kwargs):
        pk = kwargs.get("pk")
        recipe = self.get_queryset().filter(pk=pk).first()
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


# class RecipeAPIv2ListCreate(ListCreateAPIView):
#     queryset = Recipe.objects.get_published()  # type: ignore
#     serializer_class = RecipeSerializer
#     pagination_class = RecipeAPIv2Pagination

# def get(self, request: Request):
#     recipes = Recipe.objects.get_published()[:10]  # type: ignore
#     # Sempre que for retornar mais de um objeto, é necessário passar o many=True
#     serializer = RecipeSerializer(instance=recipes, many=True)
#     return Response(serializer.data)

# def post(self, request):
#     data = request.data
#     serializer = RecipeSerializer(data=data)

#     serializer.is_valid(raise_exception=True)
#     serializer.save()

#     # return Response(serializer.validated_data, status=HTTPStatus.CREATED) # isso é bom para ver as validações
#     return Response(serializer.data, status=HTTPStatus.CREATED)


# class RecipeAPIv2DetailUpdateDelete(RetrieveUpdateDestroyAPIView):
#     queryset = Recipe.objects.get_published()  # type: ignore
#     serializer_class = RecipeSerializer
#     pagination_class = RecipeAPIv2Pagination

# def get(self, request: Request, pk: int):
#     recipe = get_object_or_404(Recipe, pk=pk, is_published=True)
#     serializer = RecipeSerializer(instance=recipe, many=False)
#     return Response(serializer.data)

# Caso eu queira sobrescrever o método update

# def delete(self, request: Request, pk: int):
#     recipe = get_object_or_404(Recipe, pk=pk, is_published=True)
#     recipe.delete()
#     return Response(status=HTTPStatus.NO_CONTENT)
