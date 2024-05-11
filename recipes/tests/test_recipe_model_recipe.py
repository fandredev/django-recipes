from recipes.tests.test_recipe_base import (
    RecipeTestBase,
    Recipe,
)
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()

    def __make_recipe_no_defaults(self):
        return Recipe(
            category=self.make_category(name="Test Category"),
            author=self.make_author(username="tate"),
            title="Test",
            description="Test",
            slug="slug-for-test",
            preparation_time=10,
            preparation_time_unit="minutes",
            servings=2,
            servings_unit="people",
            preparation_step="Test",
        )
        recipe.full_clean()
        recipe.save()

    @parameterized.expand(
        [
            ("title", 65),
            ("description", 165),
            ("preparation_time_unit", 65),
            ("servings_unit", 65),
        ]
    )
    def test_recipe_fields_max_length(self, field: str, max_length: int):
        """
        Vão ser criados 4 testes, um para cada campo que tem um tamanho máximo,
        por isso o uso do @parameterized.expand

        https://pypi.org/project/parameterized/
        """
        setattr(
            self.recipe,
            field,
            "A" * (max_length + 1),
        )  # Depois que eu criei a recipe usando make_recipe no setUp, seto o valor dos campos do parametrized aqui
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()  # AQUI ACONTECE A VALIDAÇÃO (max_length)

    def test_recipe_preparation_step_is_html_false_by_default(
        self,
    ):
        recipe = self.__make_recipe_no_defaults()

        self.assertFalse(
            recipe.preparation_step_is_html,
            msg="Recipe preparation_step_is_html is not False",
        )

    def test_recipe_is_published_is_false_by_default(
        self,
    ):
        recipe = self.__make_recipe_no_defaults()

        recipe.full_clean()
        recipe.save()

        self.assertFalse(
            recipe.is_published,
            msg="Recipe is_published is not False",
        )

    def test_recipe_string_representation(self):
        self.recipe.title = "Testing representation"
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe),
            "Testing representation",
            msg="Recipe string representation must be recipe title",
        )
