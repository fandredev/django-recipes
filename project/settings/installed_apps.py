INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # DRF
    "rest_framework",
    # Apps
    "recipes",  # Isso aqui é o mesmo valor que o arquivo apps.py na propriedade name do aplicativo # noqa: E501
    "authors",
    "debug_toolbar",
    "rest_framework_simplejwt",
]
