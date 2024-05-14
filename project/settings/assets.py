from .environment import BASE_DIR
import os

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Adicione outros diretórios além do diretorio /base_static em aplicativos
STATICFILES_DIRS = (os.path.join(BASE_DIR, "base_static"),)


# Juntar arquivos estáticos globais (se tiver) e de outros apps em um único diretório # noqa: E501
STATIC_ROOT = BASE_DIR / "static"

# Configuração de mídia e juntar arquivos de mídia de outros apps em um único diretório # noqa: E501
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
