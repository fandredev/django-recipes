from django.urls import reverse
from http import HTTPStatus
from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):
    def test_recipe_home_url_is_correct(self):
        url = reverse("recipes:home")
        self.assertEqual(url, "/")

    def test_recipes_id_url_is_correct(self):
        url = reverse("recipes:recipe", kwargs={"id": 1})
        self.assertEqual(url, "/recipes/1/")

    def test_recipe_home_view_returns_status_code_200(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertTemplateUsed(response, "recipes/pages/home.html")

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertIn("No recipes found", response.content.decode())

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        self.make_recipe(is_published=False)

        response = self.client.get(reverse("recipes:home"))

        # Check if one recipe exists
        self.assertIn(
            "<h2>No recipes found here 🥲</h2>", response.content.decode("utf-8")
        )

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe(preparation_time=5)

        response = self.client.get(reverse("recipes:home"))
        response_recipes = response.context["recipes"]
        response_content = response.content.decode("utf-8")

        expected_quantity_recipes = 1

        self.assertEqual(len(response_recipes), expected_quantity_recipes)
        self.assertIn("5 Porções", response_content)
        self.assertIn("5 Minutos", response_content)
