from django.urls import reverse, resolve
from http import HTTPStatus
from recipes.views import site
from recipes.tests.test_recipe_base import (
    RecipeTestBase,
)


class RecipeDetailViewTest(RecipeTestBase):
    def test_recipe_detail_template_loads_the_correct_recipe(
        self,
    ):
        needed_title = "This is a detail page - It load one recipe"
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse("recipes:recipe", kwargs={"pk": 1}))
        content = response.content.decode("utf-8")

        self.assertIn(needed_title, content)

    def test_recipe_detail_view_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"pk": 1}))
        self.assertIs(
            view.func.view_class,
            site.RecipeDetail,
        )

    def test_recipe_detail_view_returns_404_if_no_recipe_found(
        self,
    ):
        response = self.client.get(
            reverse(
                "recipes:recipe",
                kwargs={"pk": 1000},
            )
        )
        self.assertEqual(
            response.status_code,
            HTTPStatus.NOT_FOUND,
        )
