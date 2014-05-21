logement
========

Git pour le site du logement

Development
-----------

Install [virtualenv](https://virtualenv.pypa.io/en/latest/virtualenv.html) and set up a new virtualenv:

    $ virtualenv venv
    $ . venv/bin/activate

Install the dependencies:

    $ pip install -r requirements.txt

Setup the dev database:

    $ cd src
    $ python manage.py syncdb
    $ python manage.py shell < setup/database.py

Start the devserver:

    $ python manage.py runserver

There's now a user called 'WTFO' with password 'company' you can use for development.
