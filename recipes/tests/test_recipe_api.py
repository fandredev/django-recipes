from rest_framework import test
from recipes.tests.test_recipe_base import RecipeMixin
from django.urls import reverse
from http import HTTPStatus
from unittest.mock import patch


class RecipeAPIV2Test(test.APITestCase, RecipeMixin):
    def test_recipe_api_list_returns_status_code_200(self):
        api_url = reverse("recipes:recipes-api-list")
        response = self.client.get(api_url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    @patch("recipes.views.api.RecipeAPIv2Pagination.page_size", new=7)
    def test_recipe_api_list_loads_correct_number_of_recipes(self):
        expected_number_recipes = 7
        self.make_recipe_batch(quantity=expected_number_recipes)

        response = self.client.get(reverse("recipes:recipes-api-list"))
        qtd_recipes_received = len(response.data.get("results"))  # type: ignore

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(qtd_recipes_received, expected_number_recipes)
