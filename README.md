EURECOM BDE Website [![Build Status](https://travis-ci.org/eurecombde/bde_website.svg)](https://travis-ci.org/eurecombde/bde_website)
===================

Here are developped main apps of the EURECOM BDE Website, including housing app.

Development
-----------

Install [virtualenv](https://virtualenv.pypa.io/en/latest/virtualenv.html) and set up a new virtualenv:
    
    $ virtualenv venv

Activate the virtual environment before installing dependencies, you will have to activate it each time you need to run python to use Django for the website:
    
    $ . venv/bin/activate

Install the dependencies:
    
    $ pip install -r requirements.txt

Setup the wsgi & manage files:
    
    $ cp bde_eurecom/setup/wsgi.py bde_eurecom/

Setup the dev database:
    
    $ cd bde_eurecom/setup
    $ ./setup.sh

Start the devserver:
    
    $ python manage.py runserver

There's now a user called 'WTFO' with password 'company' you can use for development.

Test
----

Install [virtualenv](https://virtualenv.pypa.io/en/latest/virtualenv.html) and set up a new virtualenv:
    
    $ virtualenv venv

Activate the virtual environment before installing dependencies, you will have to activate it each time you need to run python to use Django for the website:
    
    $ . venv/bin/activate

Install the dependencies:
    
    $ pip install -r requirements/test.txt

Setup the dev database:
    
    $ cd bde_eurecom/setup
    $ ./test.sh

Start the devserver:
    
    $ python manage.py runserver --settings=bde_eurecom.settings.test
    or 
    $ export DJANGO_SETTINGS_MODULE=bde_eurecom.settings.test
    $ python manage.py runserver

Notes
-----------
The difference between Development and Test installation is that : Development is using sqlite and Test is using mysql, but there are no problems to develop on the Test one.

To use mysql for Test, you may have to install libmysqlclient-dev

You may have to install libjpeg-dev jpeg decoder so that the PIL image library works properly.

