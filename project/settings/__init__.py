import os

if os.environ.get("DEBUG", None) is None:
    from dotenv import load_dotenv

    load_dotenv()

# flake8: noqa
from .environment import *  # isort:skip
from .assets import *  # isort:skip
from .installed_apps import *  # isort:skip
from .middlewares import *  # isort:skip
from .templates import *
from .databases import *
from .security import *
from .i18n import *
from .messages import *
from .debug_toolbar import *
from .rest_framework import *
