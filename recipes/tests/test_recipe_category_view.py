from django.urls import reverse, resolve
from recipes.tests.test_recipe_base import (
    RecipeTestBase,
)
from recipes import views
from http import HTTPStatus


class RecipeCategoryViewTest(RecipeTestBase):

    def test_recipe_category_view_function_is_correct(
        self,
    ):
        view = resolve(
            reverse(
                "recipes:category",
                kwargs={"category_id": 1000},
            )
        )
        self.assertIs(
            view.func.view_class,
            views.RecipeListViewCategory,
        )

    def test_recipe_category_view_returns_404_if_no_recipes_found(
        self,
    ):
        response = self.client.get(
            reverse(
                "recipes:category",
                kwargs={"category_id": 1000},
            )
        )

        self.assertEqual(
            response.status_code,
            HTTPStatus.NOT_FOUND,
        )

    def test_recipe_category_category_id_is_correct(
        self,
    ):
        url = reverse(
            "recipes:category",
            kwargs={"category_id": 110},
        )
        self.assertEqual(url, "/recipes/category/110/")

    def test_recipe_category_template_dont_load_recipes_not_published(
        self,
    ):
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse("recipes:recipe", kwargs={"pk": 1}))

        self.assertEqual(
            response.status_code,
            HTTPStatus.NOT_FOUND,
        )

    def test_category_template_loads_recipes(
        self,
    ):
        needed_title = "This is a category test"
        self.make_recipe(title=needed_title)

        response = self.client.get(
            reverse(
                "recipes:category",
                kwargs={"category_id": 1},
            )
        )
        content = response.content.decode("utf-8")

        self.assertIn(needed_title, content)
