from recipes.permissions import IsOwner
from ..models import Recipe

from ..serializers import RecipeSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework import request, response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404
from rest_framework import status


class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 2


class RecipeAPIV2ViewSet(ModelViewSet):
    queryset = Recipe.objects.get_published()  # type: ignore
    serializer_class = RecipeSerializer
    pagination_class = RecipeAPIv2Pagination
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    http_method_names = ["get", "post", "patch", "head", "delete"]

    def create(self, request: request.Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def get_queryset(self):
        qs = super().get_queryset()

        category_id = self.request.query_params.get("category_id", "")  # type: ignore

        if category_id != "" and category_id.isnumeric():
            qs = qs.filter(category_id=category_id)

        return qs

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get("pk", "")
        recipe = get_object_or_404(self.get_queryset(), pk=pk)

        self.check_object_permissions(self.request, recipe)

        return recipe

    def get_permissions(self):
        if self.request.method in ["PATCH", "DELETE"]:
            return [
                IsOwner(),
            ]
        return super().get_permissions()

    def partial_update(self, request: request.Request, *args, **kwargs):
        recipe = self.get_object()

        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            partial=True,
            many=False,
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
