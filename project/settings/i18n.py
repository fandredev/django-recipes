# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

from . import BASE_DIR
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True
INTERNAL_IPS = [
    "127.0.0.1",
]

LANGUAGES = (
    ("en", "English"),
    ("pt-br", "Português"),
)

LOCALE_DIR = BASE_DIR / "locale"
