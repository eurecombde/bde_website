#!/usr/bin/env bash

# Sets up the database for the project with few datas
echo -e '\n[-- CLEANED DATABASES --]\n'
rm ../../dev_db.sqlite
python ../../manage.py syncdb --noinput
echo -e '\n[-- CREATED TABLES --]\n'
python ../../manage.py shell < database.py > /dev/null
echo -e '\n[-- FILLED TABLES --]\n'
mv dev_db.sqlite ../../
