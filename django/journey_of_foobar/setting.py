import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


DEBUG = True

SECRET_KEY = '{{ secret_key }}'

SITE_URL = 'http://localhost:8000'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'DATABASE.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'KEY_PREFIX': 'localhost',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

STATIC_ROOT = '/tmp/{{ journey_of_foobar }}_static'
MEDIA_ROOT = '/tmp/{{ journey_of_foobar }}_media'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'shuwei_kuo@outlook.com'
EMAIL_HOST_PASSWORD = 'bv87m2n5'