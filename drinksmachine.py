import random
import time         #fun setup code
selecting = True

#list of drinks
drinks = 'COCA-COLA,DIET COKE,COKE ZERO,DR PEPPER,DR PEPPER ZERO,IRN BRU,IRN BRU XTRA,MONSTER ORIGINAL,MONSTER NITRO,MONSTER MANGO LOCO,MONSTER MONARCH,MONSTER ULTRA,CAPRI SUN,BLOOD OF INNOCENTS,DIET BLOOD OF INNOCENTS,CHERRY BLOOD OF INNOCENTS,BLOOD OF INNOCENTS LIME TWIST,JUST WATER,STRAWBERRY MILKSHAKE,MYSTERY SPECIAL'.split(',')

dispenseASCII = '''===========
DISPENSING:
     |
     |
     |
    ===
{0}
    ==='''

while selecting:

    choicedigit1 = input('Please select your desired drink as a two digit number (digit 1) ')
    choicedigit2 = input('Please select your desired drink (digit 2) ')

    choice = int(choicedigit1 + choicedigit2) - 1       #choosing the drink

    confirming = True

    while confirming:       #confirmation of drink
        confirmation = input('Do you want a '+drinks[choice]+' ?  OK or CANCEL ').upper()

        if confirmation == 'OK':
            confirming = False
            selecting = False

            print(dispenseASCII.format(drinks[choice]))

        if confirmation == 'CANCEL':
            confirming = False
