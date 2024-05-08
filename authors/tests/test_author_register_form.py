from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized


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
