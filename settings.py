import os
import sys
from django.contrib.messages import constants as message_constants
from dotenv import load_dotenv


load_dotenv()


# INTEGRATIONS
HOST = os.getenv("HOST")
HOST_PRETTY = os.getenv("HOST_PRETTY")
HOST_LANGUAGE = os.getenv("HOST_LANGUAGE", "en")


# COMMON
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "1"
DEV = os.getenv("DEV") == "1"
PRODUCTION = os.getenv("PRODUCTION") == "1"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
ALLOWED_HOSTS = [str(x) for x in os.getenv("ALLOWED_HOSTS").split(',') if x]
CSRF_TRUSTED_ORIGINS = [str(x) for x in os.getenv("CSRF_TRUSTED_ORIGINS").split(',') if x]
INTERNAL_IPS = [str(x) for x in os.getenv("INTERNAL_IPS").split(',') if x]
ALLOWED_WALLETS = [str(x) for x in os.getenv("ALLOWED_WALLETS").split(',') if x]

# DATABASE
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "main",
    "snippet",
    "user_profile",
)


MIDDLEWARE = [
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "site_middleware.GetUserData",
]


if DEBUG:
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]



ROOT_URLCONF = "urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.csrf",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "context_processors.common",
            ],
        },
    },
]


WSGI_APPLICATION = "wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
        "PASSWORD": POSTGRES_PASSWORD,
    }
}

MESSAGE_TAGS = {
    message_constants.DEBUG: "debug",
    message_constants.INFO: "info",
    message_constants.SUCCESS: "success",
    message_constants.WARNING: "warning",
    message_constants.ERROR: "danger",
}


# LOCALIZATION
AVAILABLE_LANGUAGES = [HOST_LANGUAGE]
LANGUAGE_CODE = HOST_LANGUAGE
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


