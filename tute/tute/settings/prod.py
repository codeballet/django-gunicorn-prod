import os
from .base import *


# Set the environment variable to:
# export DJANGO_SETTINGS_MODULE="tute.settings.prod"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '0.0.0.0']

# collect static files with command: 'python manage.py collectstatic'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")