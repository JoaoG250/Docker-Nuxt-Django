import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured


def get_env_value(env_variable):
    """Função para recuperar variável de ambiente.

    Args:
        env_variable (str): Nome da variável.

    Raises:
        ImproperlyConfigured: Levanta a exceção caso a variável não exista.

    Returns:
        str: Valor da variável de ambiente.
    """

    try:
        return str(os.environ[env_variable]).strip()
    except KeyError:
        error_msg = f"Set the {env_variable} environment variable"
        raise ImproperlyConfigured(error_msg)


ALLOWED_HOSTS = []
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECRET_KEY = get_env_value("NUXTDJANGO_SECRET_KEY")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": get_env_value("NUXTDJANGO_DATABASE_NAME"),
        "USER": get_env_value("NUXTDJANGO_DATABASE_USER"),
        "PASSWORD": get_env_value("NUXTDJANGO_DATABASE_PASSWORD"),
        "HOST": get_env_value("NUXTDJANGO_DATABASE_HOST"),
        "PORT": get_env_value("NUXTDJANGO_DATABASE_PORT"),
    }
}

if get_env_value("NUXTDJANGO_PRODUCTION") == "FALSE":
    DEBUG = True
elif get_env_value("NUXTDJANGO_PRODUCTION") == "TRUE":
    ALLOWED_HOSTS = ["*"]
    DEBUG = False
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "api.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")

# Media files

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS configuration

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
