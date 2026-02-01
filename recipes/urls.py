from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from recipes import views

app_name = "recipes"

recipe_api_v2_router = SimpleRouter()
recipe_api_v2_router.register("", views.RecipeAPIV2ViewSet, basename="recipes-api")


urlpatterns = [
    path("recipes/api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "recipes/api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("recipes/api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "",
        views.RecipeListViewHome.as_view(),
        name="home",
    ),
    path(
        "recipes/category/<int:category_id>/",
        views.RecipeListViewCategory.as_view(),
        name="category",
    ),
    path(
        "recipes/<int:pk>/",
        views.RecipeDetail.as_view(),
        name="recipe",
    ),
    path("recipes/search/", views.RecipeListViewSearch.as_view(), name="search"),  # type: ignore
    # API
    path(
        "recipes/api/v1", views.RecipeListViewHomeAPI.as_view(), name="recipes_api_v1"
    ),
    path(
        "recipes/api/v1/<int:pk>",
        views.RecipeDetailAPI.as_view(),
        name="recipes_detail_api_v1",
    ),
    path("recipes/api/v2/", include(recipe_api_v2_router.urls)),
    # path(
    #     "recipes/api/v2/",
    #     views.RecipeAPIV2ViewSet.as_view(
    #         {
    #             "get": "list",
    #             "post": "create",
    #         }
    #     ),
    #     name="recipe_api_v2_list",
    # ),
    # path(
    #     "recipes/api/v2/<int:pk>",
    #     views.RecipeAPIV2ViewSet.as_view(
    #         {
    #             "get": "retrieve",
    #             "patch": "partial_update",
    #             "delete": "destroy",
    #         }
    #     ),
    #     name="recipe_api_v2_detail",
    # ),
]
