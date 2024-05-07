from django.urls import reverse
from http import HTTPStatus
from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeSearchViewTest(RecipeTestBase):
    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse("recipes:recipe", kwargs={"id": recipe.pk}))


    def test_recipe_search_raises_for_404_if_no_search_term(self):
        response = self.client.get(reverse("recipes:search")) 
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
    
    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        query_params_value = "Test"

        response = self.client.get(reverse("recipes:search") + f"?q={query_params_value}")
        content = response.content.decode("utf-8")
        self.assertIn(f'Search for &quot;{query_params_value}&quot;', content)
