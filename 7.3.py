import csv

with open('gamer.csv', 'r') as bestand:
    readCSV = csv.reader(bestand, delimiter=';')
    scores = []
    names = []
    dates = []
    for row in readCSV:
        score = row[2]
        scores.append(score)
        name = row[0]
        names.append(name)
        date = row[1]
        dates.append(date)
        scorex = scores.index(max(scores))

        Thename = names[scorex]
        Thedate = dates[scorex]




    print (scores)
    print ('De hoogste score is:', max(scores), 'behaald door', Thename, 'op', Thedate)



