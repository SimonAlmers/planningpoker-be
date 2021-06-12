from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    '165.227.161.171',
]

DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL'])
}

INSTALLED_APPS += []