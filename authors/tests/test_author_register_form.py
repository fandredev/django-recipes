from unittest import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.test import TestCase as DjangoTestCase

from django.urls import reverse, resolve

class AuthorRegisterFormUnitTest(TestCase):

    def setUp(self):
        self.form = RegisterForm()

    @parameterized.expand(
        [
            ("email", "Your email"),
            ("username", "Your username"),
            ("first_name", "Ex.: John"),
            ("last_name", "Ex.: Doe"),
            ("password", "Type your password"),
            ("password2", "Repeat your password"),
        ]
    )
    def test_fields_placeholder_is_correct(self, field: str, expected_placeholder: str):
        current_placeholder_field = self.form[field].field.widget.attrs["placeholder"]
        self.assertEqual(expected_placeholder, current_placeholder_field)

    @parameterized.expand(
        [
            (
                "password",
                "Password must have at least one uppercase letter, one lowercase letter and one number. The length should be at least 8 characters.",
            ),
            ("email", "The e-mail must be valid"),
        ]
    )
    def test_fields_help_text_is_correct(self, field: str, expected_help_text: str):
        current_help_text_field = self.form[field].field.help_text
        self.assertEqual(expected_help_text, current_help_text_field)

    @parameterized.expand(
        [
            ("username", "User name"),
            ("first_name", "First name"),
            ("last_name", "Last name"),
            ("email", "E-mail"),
            ("password", "Password"),
            ("password2", "Password2"),
        ]
    )
    def test_fields_label(self, field: str, expected_label: str):
        current_label_field = self.form[field].field.label
        self.assertEqual(current_label_field, expected_label)


class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs) -> None:
        self.form_data = {
            "username": "test_user",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@gmail.com",
            "password": "Test@1234",
        }
        return super().setUp(*args, **kwargs)
    
    @parameterized.expand(
        [
            ("username", "This field must not be empty."),
            ('first_name', 'Write your first name.'),
            ('last_name', 'Write your last name.'),
            ('password', 'Password must not be empty.'),
            ('password2', 'Please, confirm your password.'),
            ('email', 'E-mail is required.')
        ]
    )
    def test_fields_cannot_be_empty(self, field: str, message_error: str):
        self.form_data[field] = ''
        
        url = reverse("authors:create")
        response = self.client.post(url, data=self.form_data, follow=True)
        decode_response = response.content.decode('utf-8')
        self.assertIn(message_error, decode_response)