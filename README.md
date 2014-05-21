EURECOM BDE Website
===================

Here are developped main apps of the EURECOM BDE Website, including housing app.

Development
-----------

Install [virtualenv](https://virtualenv.pypa.io/en/latest/virtualenv.html) and set up a new virtualenv:

    $ virtualenv venv
    $ . venv/bin/activate

Install the dependencies:

    $ pip install -r requirements.txt

Setup the wsgi file:

    $ cp bde_eurecom/setup/wsgi.py bde_eurecom/

Setup the dev database:

    $ cd bde_eurecom/setup
    $ chmod a+x script.sh
    $ ./script.sh

Start the devserver:

    $ python manage.py runserver

There's now a user called 'WTFO' with password 'company' you can use for development.
