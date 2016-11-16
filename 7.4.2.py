import csv

with open ('7.4.csv' , 'r') as bestand2:
    readCSV = csv.reader(bestand2, delimiter=';')
    prijzen = []
    for row in readCSV:
        prijs = row[0]
        prijzen.append(prijs)
    print (prijzen)



