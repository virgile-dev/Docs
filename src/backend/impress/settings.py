"""
Django settings for impress project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import tomllib
from socket import gethostbyname, gethostname

from django.utils.translation import gettext_lazy as _

import sentry_sdk
from configurations import Configuration, values
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join("/", "data")


def get_release():
    """
    Get the current release of the application
    """
    try:
        with open(os.path.join(BASE_DIR, "pyproject.toml"), "rb") as f:
            pyproject_data = tomllib.load(f)
        return pyproject_data["project"]["version"]
    except (FileNotFoundError, KeyError):
        return "NA"  # Default: not available


class Base(Configuration):
    """
    This is the base configuration every configuration (aka environment) should inherit from. It
    is recommended to configure third-party applications by creating a configuration mixins in
    ./configurations and compose the Base configuration with those mixins.

    It depends on an environment variable that SHOULD be defined:

    * DJANGO_SECRET_KEY

    You may also want to override default configuration by setting the following environment
    variables:

    * SENTRY_DSN
    * DB_NAME
    * DB_HOST
    * DB_PASSWORD
    * DB_USER
    """

    DEBUG = False
    USE_SWAGGER = False

    API_VERSION = "v1.0"

    # Security
    ALLOWED_HOSTS = values.ListValue([])
    SECRET_KEY = values.Value(None)
    SERVER_TO_SERVER_API_TOKENS = values.ListValue([])

    # Application definition
    ROOT_URLCONF = "impress.urls"
    WSGI_APPLICATION = "impress.wsgi.application"

    # Database
    DATABASES = {
        "default": {
            "ENGINE": values.Value(
                "django.db.backends.postgresql_psycopg2",
                environ_name="DB_ENGINE",
                environ_prefix=None,
            ),
            "NAME": values.Value(
                "impress", environ_name="DB_NAME", environ_prefix=None
            ),
            "USER": values.Value("dinum", environ_name="DB_USER", environ_prefix=None),
            "PASSWORD": values.Value(
                "pass", environ_name="DB_PASSWORD", environ_prefix=None
            ),
            "HOST": values.Value(
                "localhost", environ_name="DB_HOST", environ_prefix=None
            ),
            "PORT": values.Value(5432, environ_name="DB_PORT", environ_prefix=None),
        }
    }
    DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

    # Static files (CSS, JavaScript, Images)
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(DATA_DIR, "static")
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(DATA_DIR, "media")
    MEDIA_BASE_URL = values.Value(
        None, environ_name="MEDIA_BASE_URL", environ_prefix=None
    )

    SITE_ID = 1

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
        },
        "staticfiles": {
            "BACKEND": values.Value(
                "whitenoise.storage.CompressedManifestStaticFilesStorage",
                environ_name="STORAGES_STATICFILES_BACKEND",
            ),
        },
    }

    # Media
    AWS_S3_ENDPOINT_URL = values.Value(
        environ_name="AWS_S3_ENDPOINT_URL", environ_prefix=None
    )
    AWS_S3_ACCESS_KEY_ID = values.Value(
        environ_name="AWS_S3_ACCESS_KEY_ID", environ_prefix=None
    )
    AWS_S3_SECRET_ACCESS_KEY = values.Value(
        environ_name="AWS_S3_SECRET_ACCESS_KEY", environ_prefix=None
    )
    AWS_S3_REGION_NAME = values.Value(
        environ_name="AWS_S3_REGION_NAME", environ_prefix=None
    )
    AWS_STORAGE_BUCKET_NAME = values.Value(
        "impress-media-storage",
        environ_name="AWS_STORAGE_BUCKET_NAME",
        environ_prefix=None,
    )

    # Document images
    DOCUMENT_IMAGE_MAX_SIZE = values.Value(
        10 * (2**20),  # 10MB
        environ_name="DOCUMENT_IMAGE_MAX_SIZE",
        environ_prefix=None,
    )

    DOCUMENT_UNSAFE_MIME_TYPES = [
        # Executable Files
        "application/x-msdownload",
        "application/x-bat",
        "application/x-dosexec",
        "application/x-sh",
        "application/x-ms-dos-executable",
        "application/x-msi",
        "application/java-archive",
        "application/octet-stream",
        # Dynamic Web Pages
        "application/x-httpd-php",
        "application/x-asp",
        "application/x-aspx",
        "application/jsp",
        "application/xhtml+xml",
        "application/x-python-code",
        "application/x-perl",
        "text/html",
        "text/javascript",
        "text/x-php",
        # System Files
        "application/x-msdownload",
        "application/x-sys",
        "application/x-drv",
        "application/cpl",
        "application/x-apple-diskimage",
        # Script Files
        "application/javascript",
        "application/x-vbscript",
        "application/x-powershell",
        "application/x-shellscript",
        # Compressed/Archive Files
        "application/zip",
        "application/x-tar",
        "application/gzip",
        "application/x-bzip2",
        "application/x-7z-compressed",
        "application/x-rar",
        "application/x-rar-compressed",
        "application/x-compress",
        "application/x-lzma",
        # Macros in Documents
        "application/vnd.ms-word",
        "application/vnd.ms-excel",
        "application/vnd.ms-powerpoint",
        "application/vnd.ms-word.document.macroenabled.12",
        "application/vnd.ms-excel.sheet.macroenabled.12",
        "application/vnd.ms-powerpoint.presentation.macroenabled.12",
        # Disk Images & Virtual Disk Files
        "application/x-iso9660-image",
        "application/x-vmdk",
        "application/x-apple-diskimage",
        "application/x-dmg",
        # Other Dangerous MIME Types
        "application/x-ms-application",
        "application/x-msdownload",
        "application/x-shockwave-flash",
        "application/x-silverlight-app",
        "application/x-java-vm",
        "application/x-bittorrent",
        "application/hta",
        "application/x-csh",
        "application/x-ksh",
        "application/x-ms-regedit",
        "application/x-msdownload",
        "application/xml",
        "image/svg+xml",
    ]

    # Document versions
    DOCUMENT_VERSIONS_PAGE_SIZE = 50

    # Internationalization
    # https://docs.djangoproject.com/en/3.1/topics/i18n/

    # Languages
    LANGUAGE_CODE = values.Value("en-us")
    LANGUAGE_COOKIE_NAME = "docs_language"  # cookie & language is set from frontend

    DRF_NESTED_MULTIPART_PARSER = {
        # output of parser is converted to querydict
        # if is set to False, dict python is returned
        "querydict": False,
    }

    # Careful! Languages should be ordered by priority, as this tuple is used to get
    # fallback/default languages throughout the app.
    LANGUAGES = values.SingleNestedTupleValue(
        (
            ("en-us", _("English")),
            ("fr-fr", _("French")),
            ("de-de", _("German")),
        )
    )

    LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

    TIME_ZONE = "UTC"
    USE_I18N = True
    USE_TZ = True

    # Templates
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "OPTIONS": {
                "context_processors": [
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.csrf",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.request",
                    "django.template.context_processors.tz",
                ],
                "loaders": [
                    "django.template.loaders.filesystem.Loader",
                    "django.template.loaders.app_directories.Loader",
                ],
            },
        },
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.locale.LocaleMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "dockerflow.django.middleware.DockerflowMiddleware",
    ]

    AUTHENTICATION_BACKENDS = [
        "django.contrib.auth.backends.ModelBackend",
        "core.authentication.backends.OIDCAuthenticationBackend",
    ]

    # Django applications from the highest priority to the lowest
    INSTALLED_APPS = [
        # impress
        "core",
        "demo",
        "drf_spectacular",
        # Third party apps
        "corsheaders",
        "dockerflow.django",
        "rest_framework",
        "parler",
        "easy_thumbnails",
        # Django
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.postgres",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # OIDC third party
        "mozilla_django_oidc",
    ]

    # Cache
    CACHES = {
        "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
    }

    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "mozilla_django_oidc.contrib.drf.OIDCAuthentication",
            "rest_framework.authentication.SessionAuthentication",
        ),
        "DEFAULT_PARSER_CLASSES": [
            "rest_framework.parsers.JSONParser",
            "nested_multipart_parser.drf.DrfNestedParser",
        ],
        "EXCEPTION_HANDLER": "core.api.exception_handler",
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 20,
        "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
        "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    }

    SPECTACULAR_SETTINGS = {
        "TITLE": "Impress API",
        "DESCRIPTION": "This is the impress API schema.",
        "VERSION": "1.0.0",
        "SERVE_INCLUDE_SCHEMA": False,
        "ENABLE_DJANGO_DEPLOY_CHECK": values.BooleanValue(
            default=False,
            environ_name="SPECTACULAR_SETTINGS_ENABLE_DJANGO_DEPLOY_CHECK",
        ),
        "COMPONENT_SPLIT_REQUEST": True,
        # OTHER SETTINGS
        "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
        "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
        "REDOC_DIST": "SIDECAR",
    }

    # Mail
    EMAIL_BACKEND = values.Value("django.core.mail.backends.smtp.EmailBackend")
    EMAIL_BRAND_NAME = values.Value(None)
    EMAIL_HOST = values.Value(None)
    EMAIL_HOST_USER = values.Value(None)
    EMAIL_HOST_PASSWORD = values.Value(None)
    EMAIL_LOGO_IMG = values.Value(None)
    EMAIL_PORT = values.PositiveIntegerValue(None)
    EMAIL_USE_TLS = values.BooleanValue(False)
    EMAIL_USE_SSL = values.BooleanValue(False)
    EMAIL_FROM = values.Value("from@example.com")

    AUTH_USER_MODEL = "core.User"
    INVITATION_VALIDITY_DURATION = 604800  # 7 days, in seconds

    # CORS
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_ALL_ORIGINS = values.BooleanValue(True)
    CORS_ALLOWED_ORIGINS = values.ListValue([])
    CORS_ALLOWED_ORIGIN_REGEXES = values.ListValue([])

    # Sentry
    SENTRY_DSN = values.Value(None, environ_name="SENTRY_DSN", environ_prefix=None)

    # Collaboration
    COLLABORATION_API_URL = values.Value(
        None, environ_name="COLLABORATION_API_URL", environ_prefix=None
    )
    COLLABORATION_SERVER_SECRET = values.Value(
        None, environ_name="COLLABORATION_SERVER_SECRET", environ_prefix=None
    )
    COLLABORATION_WS_URL = values.Value(
        None, environ_name="COLLABORATION_WS_URL", environ_prefix=None
    )

    # Frontend
    FRONTEND_THEME = values.Value(
        None, environ_name="FRONTEND_THEME", environ_prefix=None
    )

    # Crisp
    CRISP_WEBSITE_ID = values.Value(
        None, environ_name="CRISP_WEBSITE_ID", environ_prefix=None
    )

    # Easy thumbnails
    THUMBNAIL_EXTENSION = "webp"
    THUMBNAIL_TRANSPARENCY_EXTENSION = "webp"
    THUMBNAIL_DEFAULT_STORAGE_ALIAS = "default"
    THUMBNAIL_ALIASES = {}

    # Celery
    CELERY_BROKER_URL = values.Value("redis://redis:6379/0")
    CELERY_BROKER_TRANSPORT_OPTIONS = values.DictValue({})

    # Session
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"
    SESSION_COOKIE_AGE = 60 * 60 * 12

    # OIDC - Authorization Code Flow
    OIDC_CREATE_USER = values.BooleanValue(
        default=True,
        environ_name="OIDC_CREATE_USER",
    )
    OIDC_RP_SIGN_ALGO = values.Value(
        "RS256", environ_name="OIDC_RP_SIGN_ALGO", environ_prefix=None
    )
    OIDC_RP_CLIENT_ID = values.Value(
        "impress", environ_name="OIDC_RP_CLIENT_ID", environ_prefix=None
    )
    OIDC_RP_CLIENT_SECRET = values.Value(
        None,
        environ_name="OIDC_RP_CLIENT_SECRET",
        environ_prefix=None,
    )
    OIDC_OP_JWKS_ENDPOINT = values.Value(
        environ_name="OIDC_OP_JWKS_ENDPOINT", environ_prefix=None
    )
    OIDC_OP_AUTHORIZATION_ENDPOINT = values.Value(
        environ_name="OIDC_OP_AUTHORIZATION_ENDPOINT", environ_prefix=None
    )
    OIDC_OP_TOKEN_ENDPOINT = values.Value(
        None, environ_name="OIDC_OP_TOKEN_ENDPOINT", environ_prefix=None
    )
    OIDC_OP_USER_ENDPOINT = values.Value(
        None, environ_name="OIDC_OP_USER_ENDPOINT", environ_prefix=None
    )
    OIDC_OP_LOGOUT_ENDPOINT = values.Value(
        None, environ_name="OIDC_OP_LOGOUT_ENDPOINT", environ_prefix=None
    )
    OIDC_AUTH_REQUEST_EXTRA_PARAMS = values.DictValue(
        {}, environ_name="OIDC_AUTH_REQUEST_EXTRA_PARAMS", environ_prefix=None
    )
    OIDC_RP_SCOPES = values.Value(
        "openid email", environ_name="OIDC_RP_SCOPES", environ_prefix=None
    )
    LOGIN_REDIRECT_URL = values.Value(
        None, environ_name="LOGIN_REDIRECT_URL", environ_prefix=None
    )
    LOGIN_REDIRECT_URL_FAILURE = values.Value(
        None, environ_name="LOGIN_REDIRECT_URL_FAILURE", environ_prefix=None
    )
    LOGOUT_REDIRECT_URL = values.Value(
        None, environ_name="LOGOUT_REDIRECT_URL", environ_prefix=None
    )
    OIDC_USE_NONCE = values.BooleanValue(
        default=True, environ_name="OIDC_USE_NONCE", environ_prefix=None
    )
    OIDC_REDIRECT_REQUIRE_HTTPS = values.BooleanValue(
        default=False, environ_name="OIDC_REDIRECT_REQUIRE_HTTPS", environ_prefix=None
    )
    OIDC_REDIRECT_ALLOWED_HOSTS = values.ListValue(
        default=[], environ_name="OIDC_REDIRECT_ALLOWED_HOSTS", environ_prefix=None
    )
    OIDC_STORE_ID_TOKEN = values.BooleanValue(
        default=True, environ_name="OIDC_STORE_ID_TOKEN", environ_prefix=None
    )
    OIDC_FALLBACK_TO_EMAIL_FOR_IDENTIFICATION = values.BooleanValue(
        default=True,
        environ_name="OIDC_FALLBACK_TO_EMAIL_FOR_IDENTIFICATION",
        environ_prefix=None,
    )

    USER_OIDC_FIELDS_TO_FULLNAME = values.ListValue(
        default=["first_name", "last_name"],
        environ_name="USER_OIDC_FIELDS_TO_FULLNAME",
        environ_prefix=None,
    )
    USER_OIDC_FIELD_TO_SHORTNAME = values.Value(
        default="first_name",
        environ_name="USER_OIDC_FIELD_TO_SHORTNAME",
        environ_prefix=None,
    )

    ALLOW_LOGOUT_GET_METHOD = values.BooleanValue(
        default=True, environ_name="ALLOW_LOGOUT_GET_METHOD", environ_prefix=None
    )

    # AI service
    AI_API_KEY = values.Value(None, environ_name="AI_API_KEY", environ_prefix=None)
    AI_BASE_URL = values.Value(None, environ_name="AI_BASE_URL", environ_prefix=None)
    AI_MODEL = values.Value(None, environ_name="AI_MODEL", environ_prefix=None)

    AI_DOCUMENT_RATE_THROTTLE_RATES = {
        "minute": 5,
        "hour": 100,
        "day": 500,
    }
    AI_USER_RATE_THROTTLE_RATES = {
        "minute": 3,
        "hour": 50,
        "day": 200,
    }

    # Y provider microservice
    # Note: Be careful, this value is currently the same as in the collaboration service.
    Y_PROVIDER_API_KEY = values.Value(
        environ_name="Y_PROVIDER_API_KEY",
        environ_prefix=None,
    )
    Y_PROVIDER_API_BASE_URL = values.Value(
        environ_name="Y_PROVIDER_API_BASE_URL",
        environ_prefix=None,
    )

    # Conversion endpoint
    CONVERSION_API_ENDPOINT = values.Value(
        default="convert-markdown",
        environ_name="CONVERSION_API_ENDPOINT",
        environ_prefix=None,
    )
    CONVERSION_API_CONTENT_FIELD = values.Value(
        default="content",
        environ_name="CONVERSION_API_CONTENT_FIELD",
        environ_prefix=None,
    )
    CONVERSION_API_TIMEOUT = values.Value(
        default=30,
        environ_name="CONVERSION_API_TIMEOUT",
        environ_prefix=None,
    )
    CONVERSION_API_SECURE = values.Value(
        default=False,
        environ_name="CONVERSION_API_SECURE",
        environ_prefix=None,
    )

    # Logging
    # We want to make it easy to log to console but by default we log production
    # to Sentry and don't want to log to console.
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": values.Value(
                    "ERROR",
                    environ_name="LOGGING_LEVEL_HANDLERS_CONSOLE",
                    environ_prefix=None,
                ),
            },
        },
        # Override root logger to send it to console
        "root": {
            "handlers": ["console"],
            "level": values.Value(
                "INFO", environ_name="LOGGING_LEVEL_LOGGERS_ROOT", environ_prefix=None
            ),
        },
        "loggers": {
            "core": {
                "handlers": ["console"],
                "level": values.Value(
                    "INFO",
                    environ_name="LOGGING_LEVEL_LOGGERS_APP",
                    environ_prefix=None,
                ),
                "propagate": False,
            },
        },
    }

    # pylint: disable=invalid-name
    @property
    def ENVIRONMENT(self):
        """Environment in which the application is launched."""
        return self.__class__.__name__.lower()

    # pylint: disable=invalid-name
    @property
    def RELEASE(self):
        """
        Return the release information.

        Delegate to the module function to enable easier testing.
        """
        return get_release()

    # pylint: disable=invalid-name
    @property
    def PARLER_LANGUAGES(self):
        """
        Return languages for Parler computed from the LANGUAGES and LANGUAGE_CODE settings.
        """
        return {
            self.SITE_ID: tuple({"code": code} for code, _name in self.LANGUAGES),
            "default": {
                "fallbacks": [self.LANGUAGE_CODE],
                "hide_untranslated": False,
            },
        }

    @classmethod
    def post_setup(cls):
        """Post setup configuration.
        This is the place where you can configure settings that require other
        settings to be loaded.
        """
        super().post_setup()

        # The SENTRY_DSN setting should be available to activate sentry for an environment
        if cls.SENTRY_DSN is not None:
            sentry_sdk.init(
                dsn=cls.SENTRY_DSN,
                environment=cls.__name__.lower(),
                release=get_release(),
                integrations=[DjangoIntegration()],
            )
            with sentry_sdk.configure_scope() as scope:
                scope.set_extra("application", "backend")


class Build(Base):
    """Settings used when the application is built.

    This environment should not be used to run the application. Just to build it with non-blocking
    settings.
    """

    SECRET_KEY = values.Value("DummyKey")
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": values.Value(
                "whitenoise.storage.CompressedManifestStaticFilesStorage",
                environ_name="STORAGES_STATICFILES_BACKEND",
            ),
        },
    }


class Development(Base):
    """
    Development environment settings

    We set DEBUG to True and configure the server to respond from all hosts.
    """

    ALLOWED_HOSTS = ["*"]
    CORS_ALLOW_ALL_ORIGINS = True
    CSRF_TRUSTED_ORIGINS = ["http://localhost:8072", "http://localhost:3000"]
    DEBUG = True

    SESSION_COOKIE_NAME = "impress_sessionid"

    USE_SWAGGER = True

    def __init__(self):
        # pylint: disable=invalid-name
        self.INSTALLED_APPS += ["django_extensions", "drf_spectacular_sidecar"]


class Test(Base):
    """Test environment settings"""

    PASSWORD_HASHERS = [
        "django.contrib.auth.hashers.MD5PasswordHasher",
    ]
    USE_SWAGGER = True

    CELERY_TASK_ALWAYS_EAGER = values.BooleanValue(True)

    def __init__(self):
        # pylint: disable=invalid-name
        self.INSTALLED_APPS += ["drf_spectacular_sidecar"]


class ContinuousIntegration(Test):
    """
    Continuous Integration environment settings

    nota bene: it should inherit from the Test environment.
    """


class Production(Base):
    """
    Production environment settings

    You must define the ALLOWED_HOSTS environment variable in Production
    configuration (and derived configurations):
    ALLOWED_HOSTS=["foo.com", "foo.fr"]
    """

    # Security
    # Add allowed host from environment variables.
    # The machine hostname is added by default,
    # it makes the application pingable by a load balancer on the same machine by example
    ALLOWED_HOSTS = [
        *values.ListValue([], environ_name="ALLOWED_HOSTS"),
        gethostbyname(gethostname()),
    ]
    CSRF_TRUSTED_ORIGINS = values.ListValue([])
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

    # SECURE_PROXY_SSL_HEADER allows to fix the scheme in Django's HttpRequest
    # object when your application is behind a reverse proxy.
    #
    # Keep this SECURE_PROXY_SSL_HEADER configuration only if :
    # - your Django app is behind a proxy.
    # - your proxy strips the X-Forwarded-Proto header from all incoming requests
    # - Your proxy sets the X-Forwarded-Proto header and sends it to Django
    #
    # In other cases, you should comment the following line to avoid security issues.
    # SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SECURE_REDIRECT_EXEMPT = [
        "^__lbheartbeat__",
        "^__heartbeat__",
    ]

    # Modern browsers require to have the `secure` attribute on cookies with `Samesite=none`
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

    # Privacy
    SECURE_REFERRER_POLICY = "same-origin"

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": values.Value(
                "redis://redis:6379/1",
                environ_name="REDIS_URL",
                environ_prefix=None,
            ),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
        },
    }


class Feature(Production):
    """
    Feature environment settings

    nota bene: it should inherit from the Production environment.
    """


class Staging(Production):
    """
    Staging environment settings

    nota bene: it should inherit from the Production environment.
    """


class PreProduction(Production):
    """
    Pre-production environment settings

    nota bene: it should inherit from the Production environment.
    """


class Demo(Production):
    """
    Demonstration environment settings

    nota bene: it should inherit from the Production environment.
    """

    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
