from django import forms
from django.contrib.auth.models import User

def add_attr(field, attr_name: str, attr_new_value: str):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f"{existing_attr} {attr_new_value}".strip()


def add_placeholder(field, placeholder: str):
    add_attr(field, 'placeholder', placeholder)

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
