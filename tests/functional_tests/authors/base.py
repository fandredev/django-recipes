from django.contrib.staticfiles.testing import (
    StaticLiveServerTestCase,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import (
    WebElement,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.browser import make_chrome_browser


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

    def wait_for(self, condition, timeout=10):
        return WebDriverWait(self.browser, timeout).until(condition)

    def wait_for_text_in_body(self, text, timeout=10):
        return self.wait_for(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), text), timeout
        )

    def _get_by_placeholder(
        self,
        web_element: WebElement,
        placeholder: str,
    ):
        return web_element.find_element(
            By.XPATH,
            f'//input[@placeholder="{placeholder}"]',
        )
