import csv
from random import randint



print ('1: Ik wil een nieuwe kluis')
print ('2: Ik wil mijn kluis openen')
print ('3: Ik geef mijn kluis terug')
print ('4: Ik wil weten hoeveel kluizen nog vrij zijn')
print ('5: Ik wil stoppen')

optie = int(input('Maak uw keuze:'))
kluisnummer = []


if optie == 1:
    with open('kluizen.csv', 'r') as file:
        readCSV = csv.reader(file, delimiter=';')
        for row in readCSV:
            kluis = row[0]
            kluisnummer.append(kluis)
    print (kluisnummer)









    #random = str(randint(0000, 9999))
   # print (random)


   # with open('kluizen.csv', 'a') as bestand:
    #    writer = csv.writer(bestand, delimiter=';')




    print ()
