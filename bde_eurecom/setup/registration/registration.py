# -*- coding: utf-8 -*-
from bde_eurecom.apps.housing.models import House, AdditionalInfo, Price, Room, Furniture, Location, Travel, Contact, Appreciation, Photo, Contributor
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
import xlrd
import unicodedata
import re
import os, random, string

#Parametre promo
PROMO = 2015
#Registration file
PROMO_FILENAME = "2015.xls"

# 3 execution types (TEST_FILE, TEST_MAIL, REGISTER)
#TEST_FILE first to check if your excel file is correctly formatted to check the outputs
#TEST_MAIL to check the rendering of your email (be sure to put yours in the parameters
#REGISTER to launch the real registration, be sure that everything is working corectly before
EXECUTION_MODE= "TEST_FILE"   

# Mail parameter
TEST_EMAIL_ADDRESS = "dudragne@eurecom.fr"
SUBJECT = "Eurecom Housing website launching"
TEXT1 ='Dear students,\n\nWho hasn\'t struggled to find and to choose the best accommodation ? And this only for a 1 year rental ! This is why I\'m very proud to announce you the launch of the Eurecom Housing website, a collaborative web platform to help the future students to find accommodations.\n\nThe idea of this website is to add the informations of your accommodation to the website, so that the future students will find easily the informations they need, in a well presented database.\nThis will be accommodations for students presented by students, so don\'t hesitate to be precise and to talk about all the drawbacks, unlike agencies that would hide the bad points. Contributions can be made exhaustive if you want to help much. Everything should be guided, go in \"My Account\" click on \"Create a new House\" and follow the instructions.\nIf you need an example, you can check the TCup apartment which is fully contributed.\n\nTime to bring your contribution now, log on the website at https://bde.eurecom.fr/housing/ with your login :'
# Credentials are included between the 2 texts
TEXT2 = 'Don\'t try to answer this email, it wouldn\'t reach anybody.\n\nIf you need to report a bug, or if you feel interested in the project and want to contribute or maintain the website, send me an email at Geoffrey.Dudragne@eurecom.fr\n\nCredits to Bastien ACHARD who co-developed the website with me.\n\nWaiting for your contribution.\nThanks to everybody.\n\nGeoffrey'

MAILX="/usr/bin/mailx"

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
    return first_name, last_name

def gen_password(length):
    chars = string.ascii_letters + string.digits
    random.seed = (os.urandom(1024))
    return ''.join(random.choice(chars) for i in range(length))

def send_mail(mail_text1, mail_text2, subject, to_address, username, password):
    custom_text=mail_text1 + "\n\nUsername : " + username + "\nPassword" + password +"\n\n"
    p = os.popen("echo %s | %s -s %s %s" % (custom_text, MAILX, subject,to_address))
    status = p.close()
    if status:
        print "Sendmail exit status", status

# ouverture du fichier Excel
wb = xlrd.open_workbook(PROMO_FILENAME)
 
# feuilles dans le classeur
sheet_names = wb.sheet_names()
print sheet_names

# lecture des donnees dans la première feuille
sh = wb.sheet_by_name(sheet_names[0])

#for rownum in range(1,sh.nrows):
for rownum in range(1,4):
    print str(rownum)
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
    password = gen_password(6)
#TEST_FILE
    if EXECUTION_MODE == "TEST_FILE":
        print "First Name : " + first_name + "\t\tLast Name : " + last_name + "\nUser name : "+ username_register +"\t\tPassword : " + password + "\nEmail : " + email + "\nPromo : "+ str(PROMO) + "\n"
#TEST_MAIL
    elif EXECUTION_MODE == "TEST_MAIL":
        send_mail(TEXT1, TEXT2, SUBJECT, TEST_EMAIL_ADDRESS, username, password)
#REGISTER
    elif EXECUTION_MODE == "REGISTER":
        add_contributor(username_register, first_name, last_name, email, PROMO, password)
        send_mail(TEXT1, TEXT2, SUBJECT, email, username, password)
#wrong parameter
    else:
        print "%s is not a valid execution mode" %EXECUTION_MODE

