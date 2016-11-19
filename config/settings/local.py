from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS += ("192.168.1.103", "192.168.1.111", )

INSTALLED_APPS += ("debug_toolbar", )

MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware", )

STATIC_ROOT = "/Users/loannguyen/.virtualenv/nikolad/static_in_env"
MEDIA_ROOT = "/Users/loannguyen/.virtualenv/nikolad/media_in_env"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY_LOCAL")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("POSTGRESQL_NAME_LOCAL"),
        'USER': get_secret("POSTGRESQL_USER_LOCAL"),
        'PASSWORD': get_secret("POSTGRESQL_PASSWORD_LOCAL"),
        'HOST': 'localhost',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

