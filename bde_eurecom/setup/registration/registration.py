# -*- coding: utf-8 -*-
from bde_eurecom.apps.housing.models import House, AdditionalInfo, Price, Room, Furniture, Location, Travel, Contact, Appreciation, Photo, Contributor
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
import xlrd
import unicodedata
import re

def add_contributor(username, first_name, last_name, email, promo, password):
    u1 = User(username=username_register, first_name=first_name, last_name=last_name, email=email)
    u1.set_password(password)
    u1.save()
    c1 = Contributor(user=u1, promo=promo)
    c1.save()

def new_username(username_base):
    username_register = username_base
    counter=0
    while User.objects.filter(username=username_register).exists():
        counter+=1
        username_register=username_base+str(counter)
    return username_register 

def parse_name(name):
    first_name="";
    last_name="";
    for w in name.split():
        if w.isupper():
            if last_name=="":
                last_name += w
            else:
                last_name += " "+w
        else:
            if first_name=="":
                first_name += w
            else:
                first_name += " "+w
    return (first_name,last_name)


#Parametre promo
PROMO = 2015

# ouverture du fichier Excel
wb = xlrd.open_workbook('2015.xls')
 
# feuilles dans le classeur
sheet_names = wb.sheet_names()
print sheet_names

# lecture des donnees dans la première feuille
sh = wb.sheet_by_name(sheet_names[0])

#for rownum in range(1,sh.nrows):
for rownum in range(1,9):
    line = sh.row_values(rownum)
    name = unicodedata.normalize('NFKD', line[0]).encode('ascii','ignore')
    parsed_name = parse_name(name)
    first_name, last_name = parse_name(name)
    email = unicodedata.normalize('NFKD', line[4]).encode('ascii','ignore')
    #as it often corresponds to canonical usernames for eurecom (and not too long), we use last name formatted in the eurecom email address as username
    match = re.search('\.(.+)@', email)
    username_base = match.group(1).lower() 
    #function below checks the database to generate an username not already existing
    username_register = new_username(username_base)
    print "First Name : " + first_name + "\nLast Name : " + last_name + "\nEmail : " + email + "\nUser name : "+ username_register + "\nPromo : "+ str(PROMO) + "\n"
    #add_contributor(username_register, first_name, last_name, email, PROMO, "azerty")

