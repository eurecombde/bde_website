from common import *

DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev_db.sqlite',
    }
}

SECRET_KEY = 'dontusethisinprod'

