"""
Django settings for oraaange project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from datetime import timedelta

import environ
from kombu import Exchange, Queue

# Django environ
root = environ.Path(__file__) - 2
env = environ.Env(
    DEBUG=(bool, True),
    PRODUCTION=(bool, False),
    SENTRY_ENABLED=(bool, False),
    SENTRY_DSN=(str,
                'https://1e039162b0354a6b83de882e66851309@sentry.io/1294170'),
    # SMSRU_ENABLED=(bool, False),
    # SMSRU_API_KEY=(str, '92A1440B-2989-5078-DE0A-905A58612D91'),
    # SMS_CODE_LIFETIME=(int, 300),
    AWS_STORAGE_BUCKET_NAME=(str, 'limon-files'),
    AWS_AUTO_CREATE_BUCKET=(bool, True),
    AWS_S3_ENDPOINT_URL=(str, 'http://storage.limonapp.com:9000'),
    REDIS_URL=(str, 'redis://localhost'),
    CLOUDAMQP_URL=(str, 'amqp://rabbit:upao0Ohr@localhost:5672/'),
    CELERY_EAGER_MODE=(bool, True),
    MAX_USERS_RADIUS=(int, 260000),
    SPM_APP_TOKEN=(str, '48796399-0936-4a15-a44e-1540a28c4cee'),
    FCM_KEY=(str, ''.join([
        'AAAAsNtfPpQ:APA91bHM7v8C2w',
        '-mX5ZKPEfyw3uoy-fRkvyUmmS1',
        'WYae2dIGHjkyZ2gzvZTK57XEdZ',
        'CqCnxYlms1oKusU_N9bCQL8McQ',
        'KHXD4Rvm7qTI7xKuvhL1MD6k89',
        'VjbPo3UogLFqHkgOlHsfZ2',
    ])),
    # For tests
    EPS=(float, 0.01),
    MINPOINTS=(int, 3),

    # Unfinished investigation about distance between points
    DISTANCE_ERROR=(float, 0.05),
)

environ.Env.read_env(env_file=root('.env'))

# Build paths inside the project like this: root('path/subdir')
BASE_DIR = root()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: don't disclose your secret key!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on on production!
DEBUG = env('DEBUG')
PRODUCTION = env('PRODUCTION')
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.gis',

    'rest_framework',
    'rest_framework_gis',
    'storages',
    'drf_yasg',
    'raven.contrib.django.raven_compat',
    'django_extensions',
    'taggit',

    'core',
    'users',
    'files',
    'locations',
    'events',
    'ads',
    'abuses',
    'contacts',
]

MIDDLEWARE = [
    'core.middlewares.JWTAuthenticationMiddleware',
    'core.middlewares.RestrictBlockedUsersMiddleware',
    'core.middlewares.RestrictUsersWithoutLocationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oraaange.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oraaange.wsgi.application'

USE_X_FORWARDED_HOST = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {'default': env.db()}
DATABASES['default']['CONN_MAX_AGE'] = 500


# PostGIS and GeoDjango
# https://postgis.net/

DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
# GDAL_LIBRARY_PATH = env('GDAL_LIBRARY_PATH')
# GEOS_LIBRARY_PATH = env('GEOS_LIBRARY_PATH')
# PROJ4_LIBRARY_PATH = env('PROJ4_LIBRARY_PATH', default=None)


# Custom user model
# https://docs.djangoproject.com/en/2.0/topics/auth/customizing

AUTH_USER_MODEL = 'users.User'
# USERNAME_FIELD = 'phone'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []
# AUTHENTICATION_BACKENDS = [
#     'core.backends.SMSCodeUserBackend',
#     'django.contrib.auth.backends.ModelBackend',
# ]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # XXX: Don't change - we use timestamps w/o TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = root('assets')
STATIC_URL = '/static/'

STATICFILES_DIRS = (root('static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = root('media')


# Fixtures
# https://docs.djangoproject.com/en/1.10/howto/initial-data/

FIXTURE_DIRS = (root('fixtures'),)


# Django REST Framework
# http://www.django-rest-framework.org

REST_FRAMEWORK = {
    'DATETIME_FORMAT': '%s',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 'EXCEPTION_HANDLER': 'core.utils.custom_exception_handler',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}


# Celery
# http://docs.celeryproject.org

CELERY_BROKER_URL = env('CLOUDAMQP_URL', default=env('REDIS_URL'))
CELERY_BROKER_CONNECTION_TIMEOUT = 30
CELERY_TASK_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('pushes',  Exchange('pushes'), routing_key='pushes',
          queue_arguments={'x-max-priority': 10}),
    Queue('media',  Exchange('media'), routing_key='media'),
)
CELERY_TASK_ROUTES = {
    'chats.tasks.send_*': {
        'queue': 'pushes',
        'routing_key': 'pushes',
    },
    'files.tasks.*': {
        'queue': 'media',
        'routing_key': 'media',
    },
}
CELERY_TASK_DEFAULT_QUEUE = 'default'
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_TASK_DEFAULT_ROUTING_KEY = 'default'
CELERY_TASK_ALWAYS_EAGER = env('CELERY_EAGER_MODE')

# Geolocation with GeoIP2
# https://docs.djangoproject.com/ko/2.0/ref/contrib/gis/geoip2/

GEOIP_PATH = root('contrib')


# JWT Auth
# https://getblimp.github.io/django-rest-framework-jwt/

JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_EXPIRATION_DELTA': timedelta(days=30),
    'JWT_ALLOW_REFRESH': True,
    'JWT_PAYLOAD_HANDLER': 'core.handlers.custom_jwt_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'core.handlers.custom_jwt_response_handler',
}


# Yet another Swagger generator
# https://drf-yasg.readthedocs.io/en/stable/index.html

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        },
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'DOC_EXPANSION': 'none',
    'USE_SESSION_AUTH': False,
    'SHOW_COMMON_EXTENSIONS': False,
    'DEFAULT_MODEL_RENDERING': 'example',
}


# Sentry
# https://sentry.io/welcome/

if env('SENTRY_ENABLED'):
    RAVEN_CONFIG = {
        'dsn': env('SENTRY_DSN'),
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        # 'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
    }


# Django storages
# https://django-storages.readthedocs.io

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_AUTO_CREATE_BUCKET = env('AWS_AUTO_CREATE_BUCKET', default=True)
AWS_S3_ENDPOINT_URL = env('AWS_S3_ENDPOINT_URL')
AWS_QUERYSTRING_AUTH = False


# SMS.ru gateway
# https://sms.ru
#
# SMSRU_ENABLED = env('SMSRU_ENABLED')
# SMSRU_API_KEY = env('SMSRU_API_KEY')

# FCM
# https://github.com/olucurious/PyFCM
FCM_KEY = env("FCM_KEY")


# Additional settings

# SMS_CODE_LIFETIME = env('SMS_CODE_LIFETIME')
MAX_USERS_RADIUS = env('MAX_USERS_RADIUS')
EPS = env('EPS')
MINPOINTS = env('MINPOINTS')
SPM_APP_TOKEN = env('SPM_APP_TOKEN')

# Set this to True to wrap each view in a transaction on this database.
# Related discussion link
#   https://chat.limonapp.com/channel/coding?msg=gmBwfAo9o8qGnNHno
ATOMIC_REQUESTS = True
