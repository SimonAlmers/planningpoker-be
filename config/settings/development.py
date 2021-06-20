from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "test_db",
        "TEST": {"NAME": "development_db"},
    }
}

INSTALLED_APPS += []
