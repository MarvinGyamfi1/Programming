import datetime
import csv
naam = ''
gbdatum = ''
email = ''





def test():

    file = open('inloggers.csv', 'a')
    writer = csv.writer(file, delimiter=';')
    writer.writerow('')

    naam = input('Wat is je achternaam?:')
    voorl = input('Wat zijn je voorletters?:')
    gbdatum = input('Wat is je geboortedatum?:')
    email = input('Wat is je e-mail adres?:')

    file.write(naam)
    file.write(voorl)
    file.write(gbdatum)
    file.write(email)
    print ('opgeslagen!')

while naam != 'einde':

    test()












