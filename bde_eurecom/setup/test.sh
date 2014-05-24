#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE=bde_eurecom.settings.test

echo -e '\n[-- CLEANING TABLES --]\n'
mysql -u wtfo -pcompany -e "DROP DATABASE IF EXISTS housing; CREATE DATABASE housing"

# Sets up the database for the project with few datas
echo -e '\n[-- CREATING TABLES --]\n'
python ../../manage.py syncdb --noinput
python ../../manage.py migrate --noinput bde_eurecom.apps.housing

echo -e '\n[-- FILLING TABLES --]\n'
echo "import bde_eurecom.setup.database" | python ../../manage.py shell > /dev/null

