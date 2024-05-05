from django.urls import reverse, resolve
from http import HTTPStatus
from recipes import views, models
from recipes.tests.test_recipe_base import RecipeTestBase
from unittest import skip


class RecipesURLsTest(RecipeTestBase):
    def test_recipe_home_url_is_correct(self):
        url = reverse("recipes:home")
        self.assertEqual(url, "/")

    def test_recipe_category_home_url_is_correct(self):
        url = reverse("recipes:category", kwargs={"category_id": 110})
        self.assertEqual(url, "/recipes/category/110/")

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

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe(preparation_time=5)

        response = self.client.get(reverse("recipes:home"))
        response_recipes = response.context["recipes"]
        response_content = response.content.decode("utf-8")

        expected_quantity_recipes = 1

        self.assertEqual(len(response_recipes), expected_quantity_recipes)
        self.assertIn("5 Porções", response_content)
        self.assertIn("5 Minutos", response_content)

    def test_category_template_loads_recipes(self):
        needed_title = "This is a category test"
        self.make_recipe(title=needed_title)

        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": 1})
        )
        content = response.content.decode("utf-8")

        expected_quantity_recipes = 1

        self.assertIn(needed_title, content)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = "This is a detail page - It load one recipe"
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse("recipes:recipe", kwargs={"id": 1}))
        content = response.content.decode("utf-8")

        expected_quantity_recipes = 1

        self.assertIn(needed_title, content)

    def test_recipe_detail_view_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"id": 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": 1000})
        )
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_recipe_detail_view_returns_404_if_no_recipe_found(self):
        response = self.client.get(reverse("recipes:recipe", kwargs={"id": 1000}))
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        self.make_recipe(is_published=False)

        response = self.client.get(reverse("recipes:home"))

        # Check if one recipe exists
        self.assertIn(
            "<h2>No recipes found here 🥲</h2>", response.content.decode("utf-8")
        )

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse("recipes:recipe", kwargs={"id": recipe.id}))

    @skip("Always skips")
    def test_pytest_skip(self):
        self.fail("Always fails")
