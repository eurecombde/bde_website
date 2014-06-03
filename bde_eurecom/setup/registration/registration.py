# -*- coding: utf-8 -*-
import xlrd
import unicodedata
import re


# ouverture du fichier Excel
wb = xlrd.open_workbook('2015.xls')
 
# feuilles dans le classeur
sheet_names = wb.sheet_names()
print sheet_names

# lecture des donnees dans la première feuille
sh = wb.sheet_by_name(sheet_names[0])

for rownum in range(1,sh.nrows):
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
    mail = unicodedata.normalize('NFKD', line[4]).encode('ascii','ignore')
    match = re.search('\.(.+)@', mail)
    username = match.group(1).lower()
    promo = 2015
    print "First Name : " + first_name + "\nLast Name : " + last_name + "\nEmail : " + mail + "\nUser name : "+ username + "\nPromo : "+ str(promo) + "\n"
