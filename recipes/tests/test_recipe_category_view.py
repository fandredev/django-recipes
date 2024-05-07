from django.urls import reverse
from recipes.tests.test_recipe_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):

    def test_recipe_category_home_url_is_correct(self):
        url = reverse("recipes:category", kwargs={"category_id": 110})
        self.assertEqual(url, "/recipes/category/110/")


    def test_category_template_loads_recipes(self):
        needed_title = "This is a category test"
        self.make_recipe(title=needed_title)

        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": 1})
        )
        content = response.content.decode("utf-8")

        self.assertIn(needed_title, content)
