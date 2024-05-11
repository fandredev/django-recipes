from django.contrib.staticfiles.testing import (
    StaticLiveServerTestCase,
)
from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import (
    WebElement,
)


class AuthorsBaseTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds: int = 5):
        import time

        time.sleep(seconds)

    def _get_by_placeholder(
        self,
        web_element: WebElement,
        placeholder: str,
    ):
        return web_element.find_element(
            By.XPATH,
            f'//input[@placeholder="{placeholder}"]',
        )
