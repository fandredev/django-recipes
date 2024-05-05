from django.test import TestCase
from django.urls import reverse


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

    