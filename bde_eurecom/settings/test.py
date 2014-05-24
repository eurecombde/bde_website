from common import *

DEBUG = True

TEMPLATE_DEBUG = True

SECRET_KEY = 'bouyah'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'housing',
        'USER' : 'wtfo',
        'PASSWORD' : 'company',
        'HOST' : '127.0.0.1',
    }
}
