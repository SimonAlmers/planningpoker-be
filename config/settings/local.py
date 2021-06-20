from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "165.227.161.171",
]

# DJANGO CORS HEADERS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

DATABASES = {"default": dj_database_url.config(default=os.environ["DATABASE_URL"])}

INSTALLED_APPS += []
