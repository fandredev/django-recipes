from rest_framework import test
from recipes.tests.test_recipe_base import RecipeMixin
from django.urls import reverse
from http import HTTPStatus
from unittest.mock import patch
from faker import Faker


class RecipeAPIV2Test(test.APITestCase, RecipeMixin):

    def setUp(self):
        self.faker = Faker()

    def __get_recipe_reverse_url(self, reverse_result=None) -> str:
        api_url = reverse_result or reverse("recipes:recipes-api-list")

        return api_url

    def __get_recipe_api_list(self, reverse_result=None):
        api_url = self.__get_recipe_reverse_url(reverse_result)
        response = self.client.get(api_url)
        return response

    def test_recipe_api_list_returns_status_code_200(self):
        response = self.__get_recipe_api_list()

        self.assertEqual(response.status_code, HTTPStatus.OK)

    @patch("recipes.views.api.RecipeAPIv2Pagination.page_size", new=7)
    def test_recipe_api_list_loads_correct_number_of_recipes(self):
        expected_number_recipes = 7
        self.make_recipe_batch(quantity=expected_number_recipes)

        response = self.client.get(reverse("recipes:recipes-api-list"))
        qtd_recipes_received = len(response.data.get("results"))  # type: ignore

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(qtd_recipes_received, expected_number_recipes)

    @patch("recipes.views.api.RecipeAPIv2Pagination.page_size", new=10)
    def test_recipe_api_list_loads_recipes_by_category_id(self):
        # Creates categories
        category_wanted = self.make_category(name="WANTED_CATEGORY")
        category_not_wanted = self.make_category(name="NOT_WANTED_CATEGORY")

        # Creates 10 recipes
        recipes = self.make_recipe_batch(quantity=10)

        # Change all recipes to the wanted category
        for recipe in recipes:
            recipe.category = category_wanted
            recipe.save()

        # Change one recipe to the NOT wanted category
        # As a result, this recipe should NOT show in the page
        recipes[0].category = category_not_wanted
        recipes[0].save()

        # Action: get recipes by wanted category_id
        api_url = (
            reverse("recipes:recipes-api-list") + f"?category_id={category_wanted.id}"  # type: ignore
        )
        response = self.__get_recipe_api_list(reverse_result=api_url)

        # We should only see recipes from the wanted category
        self.assertEqual(len(response.data.get("results")), 9)  # type: ignore

    def test_recipe_api_list_user_must_send_jwt_token_to_create_recipe(self):
        api_url = self.__get_recipe_reverse_url()
        response = self.client.post(api_url)

        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)
