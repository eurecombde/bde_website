# -*- coding: utf-8 -*-
from bde_eurecom.apps.housing.models import House, AdditionalInfo, Price, Room, Furniture, Location, Travel, Contact, Appreciation, Photo, Contributor
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
import xlrd
import unicodedata
import re

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
    last_name="";
    first_name="";
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
    email = unicodedata.normalize('NFKD', line[4]).encode('ascii','ignore')
    match = re.search('\.(.+)@', email)
    username_base = match.group(1).lower()
    username_register = username_base
    counter=0
    while User.objects.filter(username=username_register).exists():
        counter+=1
        username_register=username_base+str(counter)
    print "First Name : " + first_name + "\nLast Name : " + last_name + "\nEmail : " + email + "\nUser name : "+ username_register + "\nPromo : "+ str(PROMO) + "\n"
    u1 = User(username=username_register, first_name=first_name, last_name=last_name, email=email)
    u1.set_password("azerty")
    u1.save()
    c1 = Contributor(user=u1)
    c1.save()

