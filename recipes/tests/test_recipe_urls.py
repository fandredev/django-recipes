from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from http import HTTPStatus


class RecipesURLsTest(TestCase):

    def test_recipe_home_url_is_correct(self):
        url = reverse("recipes:home")
        self.assertEqual(url, "/")

    def test_recipe_category_home_url_is_correct(self):
        url = reverse("recipes:category", kwargs={"category_id": 1})
        self.assertEqual(url, "/recipes/category/1/")

    def test_recipes_id_url_is_correct(self):
        url = reverse("recipes:recipe", kwargs={"id": 1})
        self.assertEqual(url, "/recipes/1/")

    def test_recipe_search_url_is_correct(self):
        url = reverse("recipes:search")
        self.assertEqual(url, "/recipes/search/")

    def test_recipe_search_uses_correct_view(self):
        url = reverse("recipes:search")
        resolved = resolve(url)

        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse("recipes:search") + "?q=teste")
        self.assertTemplateUsed(response, "recipes/pages/search.html")
