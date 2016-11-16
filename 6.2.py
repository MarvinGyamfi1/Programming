


with open('ticker.txt', 'r') as file:
    test = {}
    for x in file:
        (key, val) = x.split(':')
        test[str(key)] = val

print (test)

bedrijf = input('Enter Company name:')
for name, afkorting in test.items():
    if bedrijf == name :
        print (afkorting)



