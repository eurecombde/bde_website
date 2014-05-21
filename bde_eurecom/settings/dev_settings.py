from src.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev_db.sqlite',
    }
}

SECRET_KEY = 'dontusethisinprod'
