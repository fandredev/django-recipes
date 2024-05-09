from .base import AuthorsBaseTest
import pytest


@pytest.mark.functional
class AuthorsRegisterTest(AuthorsBaseTest):
    def test_register_author(self):
        self.browser.get(self.live_server_url + "/authors/register/")
        self.sleep()
