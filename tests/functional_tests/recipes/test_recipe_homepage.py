from unittest.mock import patch

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from .base import RecipeBaseFunctionalTest


@pytest.mark.functional
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    @patch("recipes.views.PER_PAGE", new=3)
    def test_recipe_homepage_without_recipes_not_found_message(
        self,
    ):
        self.browser.get(self.live_server_url)

        self.wait_for_text_in_body("No recipes found here")

    @patch("recipes.views.PER_PAGE", new=3)
    def test_recipe_search_input_can_find_correct_recipes(
        self,
    ):
        recipes = self.make_recipe_batch(8)

        title_needed = "Random title"
        recipes[0].title = title_needed
        recipes[0].save()

        # Usuário open homepages
        self.browser.get(self.live_server_url)

        # User view the search input with placeholder "Search for a recipe"
        search_input = self.browser.find_element(
            By.XPATH,
            "//input[@placeholder='Search for a recipe']",
        )

        # Click on the search input and type "Recipe Title 1" to find the recipe with this title
        search_input.send_keys(recipes[0].title)
        search_input.send_keys(Keys.ENTER)

        self.assertEqual(title_needed, recipes[0].title)
        self.wait_for(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "main-content-list"), title_needed
            )
        )

    @patch("recipes.views.site.PER_PAGE", new=2)
    def test_recipe_home_page_pagination(self):
        self.make_recipe_batch()

        # Usuário abre a página
        self.browser.get(self.live_server_url)

        # Vê que tem uma paginação e clica na página 2
        page2 = self.browser.find_element(
            By.XPATH,
            '//a[@aria-label="Go to page 2"]',
        )
        page2.click()

        # Vê que tem mais 2 receitas na página 2
        self.wait_for(lambda br: len(br.find_elements(By.CLASS_NAME, "recipe")) == 2)
