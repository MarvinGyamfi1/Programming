import random

def monopolyworp():

    worp_1 = random.randrange(1,3)
    worp_2 = random.randrange(1,3)
    samen = worp_1 + worp_2
    if worp_1 != worp_2:
        print (worp_1, '+', worp_2, '=', samen)
    if worp_1 == worp_2:
        print (worp_1, '+', worp_2, '=', samen, '(dubbel)')
        monopolyworp()







monopolyworp()

