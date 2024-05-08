from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

def add_attr(field, attr_name: str, attr_new_value: str):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f"{existing_attr} {attr_new_value}".strip()


def add_placeholder(field, placeholder: str):
    add_attr(field, 'placeholder', placeholder)

def strong_password(password: str):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
            code='invalid'
        )

class RegisterForm(forms.ModelForm):

# 1 FORMA PARA PERSONALIZAR O FORMULÁRIO:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_placeholder(self.fields["email"], 'Your email')
        add_placeholder(self.fields["username"], 'Your username')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')


# 2 FORMA PARA PERSONALIZAR O FORMULÁRIO:

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Your password",
            }
        ),
        error_messages={
            "required": "This field must not be empty.",
            "max_length": "This field must have a maximum of 150 characters.",
        },
        help_text="Password must have at least one uppercase letter, one lowercase letter and one number. The length should be at least 8 characters.",
        validators=[strong_password] # Validador customizado
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Type your password",
            }
        )
    )

# 3 FORMA PARA PERSONALIZAR O FORMULÁRIO:

    class Meta:
        model = User
        # exclude = ['password'] # Quais campos não aparecem no form

        fields = [
            "first_name",
            "username",
            "last_name",
            "email",
            "password",
        ]  # Quais campos aparecem no form

        labels = {  # Como ficará a label de cada campo
            "first_name": "First name",
            "last_name": "Lastname",
            "username": "Username",
            "email": "Email",
            "password": "Password",
        }

        # Texto de ajuda abaixo do campo
        help_texts = {"email": "The e-mail must be valid"}

        # Personalizando as mensagens de erro
        error_messages = {
            "username": {
                "unique": "This username is already in use. Please, choose another one.",
                "required": "This field must not be empty.",
                "max_length": "This field must have a maximum of 150 characters.",
                "invalid": "Enter a valid username.",
            }
        }

        # Personalizar os campos do formulário
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control more-class-here",
                    "placeholder": "Type your username here",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "placeholder": "Type your password here",
                }
            ),
        }

    # Validando o campo password do formulário (SEMPRE USAR O PREFIXO clean_+nome_do_campo)
    def clean_password(self):
        data = self.cleaned_data.get("password")

        if 'atenção' in data: # type: ignore
            raise ValidationError("The password must not contain the word 'atenção'.", code="invalid")

        return data
    

    # Validando o campo first_name do formulário (SEMPRE USAR O PREFIXO clean_+nome_do_campo)
    def clean_first_name(self):
        data = self.cleaned_data.get("first_name")

        if 'John Doe' in data: # type: ignore
            raise ValidationError("The first_name must not contain the word %(value)s.", code="invalid", params={'value': "'John Doe'"})

        return data
    

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                    # more errors here if needed
                ],
            })