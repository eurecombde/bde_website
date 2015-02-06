"""
    Run this file with `fab deploy` to deploy changes to the server. Note that the server will
    fetch changes from the GitHub repo, so you have to push your changes there for them to have
    any effect.
"""

from fabric.api import local, cd, env, sudo
from getpass import getpass

password = getpass('Enter password for eurecom user at bde.eurecom.fr: ')

env.password = password
env.user = 'eurecom'
env.hosts = ['bde.eurecom.fr']


def test():
    local('python manage.py test')


def deploy():
    #test()
    with cd('/var/www/bde_website'):
        sudo('git pull origin master')
        sudo('/opt/virtualenvs/bde_eurecom/bin/pip install -r requirements/prod.txt')
        sudo('/opt/virtualenvs/bde_eurecom/bin/python manage.py migrate housing --settings=bde_eurecom.settings.prod')
        sudo('/opt/virtualenvs/bde_eurecom/bin/python manage.py collectstatic --noinput --settings=bde_eurecom.settings.prod')
        sudo('service apache2 restart')
