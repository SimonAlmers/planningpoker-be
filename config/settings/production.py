from .base import *

DEBUG = False 

ALLOWED_HOSTS = [ "api-planningpoker.simonalmers.dev", ]

# DJANGO CORS HEADERS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://planningpoker.simonalmers.dev",
    "https://develop-planningpoker.simonalmers.dev",
]

DATABASES = {"default": dj_database_url.config(default=os.environ["DATABASE_URL"])}

INSTALLED_APPS += []