from .base import AuthorsBaseTest
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from faker import Faker


@pytest.mark.functional
class AuthorsRegisterTest(AuthorsBaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faker = Faker()

    def __fill_form_dummy_data(self, form: WebElement):

        fields = form.find_elements(By.TAG_NAME, "input")

        for field in fields:
            if field.is_displayed():
                field.send_keys(" " * 20)

    def __get_form(self):
        return self.browser.find_element(By.XPATH, "/html/body/main/div[2]/form")

    def __form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + "/authors/register/")

        form = self.__get_form()

        self.__fill_form_dummy_data(form)
        form.find_element(By.NAME, "email").send_keys("dummy@email.com")

        callback(form)

        return form

    def test_empty_first_name_error_message(self):
        def callback(form: WebElement):
            first_name_field = self._get_by_placeholder(form, "Ex.: John")
            first_name_field.send_keys(" ")
            first_name_field.send_keys(Keys.ENTER)

            form = self.__get_form()

            self.assertIn("Write your first name", form.text)

        self.__form_field_test_with_callback(callback)

    def test_empty_last_name_error_message(self):
        def callback(form: WebElement):
            last_name_field = self._get_by_placeholder(form, "Ex.: Doe")
            last_name_field.send_keys(" ")
            last_name_field.send_keys(Keys.ENTER)

            form = self.__get_form()

            self.assertIn("Write your last name", form.text)

        self.__form_field_test_with_callback(callback)

    def test_empty_username_error_message(self):
        def callback(form: WebElement):
            last_name_field = self._get_by_placeholder(form, "Your username")
            last_name_field.send_keys(" ")
            last_name_field.send_keys(Keys.ENTER)

            form = self.__get_form()

            self.assertIn("This field must not be empty", form.text)

        self.__form_field_test_with_callback(callback)

    def test_invalid_email_error_message(self):
        def callback(form: WebElement):
            email_field = self._get_by_placeholder(form, "Your e-mail")
            email_field.send_keys(" ")
            email_field.send_keys(Keys.ENTER)

            form = self.__get_form()

            self.assertIn("The e-mail must be valid", form.text)

        self.__form_field_test_with_callback(callback)

    def test_passwords_do_not_match(self):
        def callback(form):
            password1 = self._get_by_placeholder(form, "Type your password")
            password2 = self._get_by_placeholder(form, "Repeat your password")
            password1.send_keys("P@ssw0rd")
            password2.send_keys("P@ssw0rd_Different")
            password2.send_keys(Keys.ENTER)
            form = self.__get_form()
            self.assertIn("Password and password2 must be equal", form.text)

        self.__form_field_test_with_callback(callback)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + "/authors/register/")

        form = self.__get_form()

        self._get_by_placeholder(form, "Ex.: John").send_keys(self.faker.first_name())
        self._get_by_placeholder(form, "Ex.: Doe").send_keys(self.faker.last_name())
        self._get_by_placeholder(form, "Your username").send_keys(
            self.faker.last_name_male()
        )
        self._get_by_placeholder(form, "Your e-mail").send_keys(self.faker.email())
        self._get_by_placeholder(form, "Type your password").send_keys("P@ssw0rd1")
        self._get_by_placeholder(form, "Repeat your password").send_keys("P@ssw0rd1")

        form.submit()

        self.assertIn(
            "User registered successfully",
            self.browser.find_element(By.TAG_NAME, "body").text,
        )
