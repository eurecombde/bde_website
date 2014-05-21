"""
Django settings for bde_eurecom project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

ADMINS = (
    ('nobu42', 'achard@eurecom.fr'),
    ('gd', 'dudragne@eurecom.fr'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev_db.sqlite',
    }
}

SECRET_KEY = 'dontusethisinprod'

