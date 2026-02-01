from http import HTTPStatus

from django.urls import reverse

from recipes.tests.test_recipe_base import (
    RecipeTestBase,
)


class RecipeSearchViewTest(RecipeTestBase):
    def test_recipe_detail_template_dont_load_recipe_not_published(
        self,
    ):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                "recipes:recipe",
                kwargs={"pk": recipe.pk},
            )
        )
        self.assertEqual(
            response.status_code,
            HTTPStatus.NOT_FOUND,
        )

    def test_recipe_search_raises_for_404_if_no_search_term(
        self,
    ):
        response = self.client.get(reverse("recipes:search"))
        self.assertEqual(
            response.status_code,
            HTTPStatus.NOT_FOUND,
        )

    def test_recipe_search_term_is_on_page_title_and_escaped(
        self,
    ):
        query_params_value = "Test"

        response = self.client.get(
            reverse("recipes:search") + f"?q={query_params_value}"
        )
        content = response.content.decode("utf-8")
        self.assertIn(
            f"Search for &quot;{query_params_value}&quot;",
            content,
        )

    def test_recipe_search_can_find_recipe_by_title(
        self,
    ):
        title1 = "This is recipe one"
        title2 = "This is recipe two"

        recipe1 = self.make_recipe(
            slug="one",
            title=title1,
            author_data={"username": "one"},
        )
        recipe2 = self.make_recipe(
            slug="two",
            title=title2,
            author_data={"username": "two"},
        )

        search_url = reverse("recipes:search")
        response1 = self.client.get(f"{search_url}?q={title1}")
        response2 = self.client.get(f"{search_url}?q={title2}")
        response_both = self.client.get(f"{search_url}?q=this")

        self.assertIn(recipe1, response1.context["recipes"])
        self.assertNotIn(recipe2, response1.context["recipes"])

        self.assertIn(recipe2, response2.context["recipes"])
        self.assertNotIn(recipe1, response2.context["recipes"])

        self.assertIn(
            recipe1,
            response_both.context["recipes"],
        )
        self.assertIn(
            recipe2,
            response_both.context["recipes"],
        )
