import os

from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", 'django-insecure-2ybunybny*27r$t^!u%jw^v1!smq@180)nm1nwi+ww3^a&9@_c')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", 0))

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", 'localhost 127.0.0.1').split(" ")
