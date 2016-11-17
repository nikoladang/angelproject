from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = True

ALLOWED_HOSTS += ("www.nikolad.com","nikolad.com",)

STATIC_ROOT = os.path.join(BASE_DIR, "../staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "../media")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY_PRODUCTION")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("POSTGRESQL_NAME_PRODUCTION"),
        'USER': get_secret("POSTGRESQL_USER_PRODUCTION"),
        'PASSWORD': get_secret("POSTGRESQL_PASSWORD_PRODUCTION"),
        'HOST': 'localhost',
        'PORT': '',
    }
}


