name = {'bob':0, 'mathijs':0}

def namen():

    geef_naam = str(input('Geef je naam:'))
    while geef_naam != '':
        geef_naam = str(input('Volgende naam:'))
        for naam, aantal in name.items():
            if geef_naam == naam:
                aantal += 1

        if geef_naam is '':
            print (name)
            break
namen()

