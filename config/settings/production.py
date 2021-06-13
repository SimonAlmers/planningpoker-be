from .base import *

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {"default": dj_database_url.config(default=os.environ["DATABASE_URL"])}

INSTALLED_APPS += []
