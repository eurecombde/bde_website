#!/usr/bin/env bash

# Sets up the database for the project with few datas
echo -e '\n[-- CLEANING DATABASES --]\n'
if [ -e ../../dev_db.sqlite ]; then
    rm ../../dev_db.sqlite
fi

echo -e '\n[-- CREATING TABLES --]\n'
python ../../manage.py syncdb --noinput
python ../../manage.py migrate --noinput bde_eurecom.apps.housing

echo -e '\n[-- FILLING TABLES --]\n'
python ../../manage.py shell < database.py > /dev/null
mv dev_db.sqlite ../../
