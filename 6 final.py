#Deel 1
naam = input('Wat is uw naam?:')
beginstation = input('Wat is uw beginstation?:')
eindstation = input('Wat is uw eindstation?')
invoerstring = naam + beginstation + eindstation


def code(invoerstring):
    for item in invoerstring:
        plusdrie = (ord(item)+3)
        print(chr(plusdrie), end = '')
print(code(invoerstring))
print()

#Deel 2
Kolom = ['', 'Geordend', 'Muteerbaar', 'Iterable', 'Dubbele waarden toegestaan']
Tuple = ['Tuple', 'Niet geordend', 'Niet muteerbaar', 'Iterable','Dubbele waarden toegestaan']
Dictionary = ['Dictionary', 'Niet geordend', 'Muteerbaar', 'Iterable', 'Keys dubbel toegestaan, Values dubbel niet toegestaan']
Set = ['Set', 'Geordend', 'Niet muteerbaar', 'Iterable', 'Geen dubbele toegestaan']
List = ['List', 'Niet geordend', 'Muteerbaar', 'Iterable', 'Dubbele toegestaan']
Lijst = [Kolom, Tuple, Dictionary, Set, List]
for item in Lijst:
    print('{0:12}{1:16}{2:17}{3:10}{4:20}'.format(item[0], item[1], item[2], item[3], item[4]))
