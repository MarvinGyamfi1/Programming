import csv

with open('7.4.csv' , 'a') as bestand:
    while True:
        writer = csv.writer(bestand, delimiter=';')
        writer.writerow(('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))
        Anummer = input('Artikelnummer?:')
        if Anummer is '':
            break
        Acode = input('Code?:')
        name = input('Naam?:')
        voorraad = input('Voorraad?:')
        prijs = input('Prijs?:')
        writer.writerow((Anummer, Acode, name, voorraad, prijs))
bestand.close()


