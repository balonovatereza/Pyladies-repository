import random

SLOVO = ''
NEUSPESNY_POKUS = 0
POLE = '_' * len(SLOVO)


def kresli_obesence(neuspesny_pokus):
    '''Na zaklade neuspesnych pokusu vypise obrazek obesence.'''

    with open(str(neuspesny_pokus) + '.txt', encoding='utf-8') as soubor:
        print(soubor.read())


def vyhodnot(pole, neuspesny_pokus):
    '''Podle poctu neuspesnych pokusu a stavu herniho pole vrati:
    '-' - pokud hra dale pokracuje
    '!' - pokud hra konci (hrac vyhral nebo prohral)'''

    if neuspesny_pokus == 10:
        print('Konec hry, prohral jsi.')
        return '!'
    elif '_' not in pole:
        print('Vyhral jsi.')
        return '!'
    else:
        return '-'


def vyber_slovo():
    '''Ze zadanych slov nahodne vybere slovo.'''

    slova = ['smudla', 'profa', 'kejchal', 'rejpal', 'stydlin', 'stistko',
             'drimal', 'snehurka']
    slovo = random.choice(slova)
    print(slovo)
    return slovo


def tah(pole, slovo, neuspesny_pokus):
    '''Zepta se hrace na pismenko a vrati herni pole se zaznamenanym tahem
     a upraveny pocet neuspesnych pokusu'''

    pismeno = input('Hadej pismeno: ').strip()

    if pismeno in slovo:
        pole = pole[:slovo.index(pismeno)] + pismeno + pole[slovo.index(pismeno) + 1:]
        return pole, neuspesny_pokus
    elif pismeno not in slovo:
        neuspesny_pokus += 1
        kresli_obesence(neuspesny_pokus)
        return pole, neuspesny_pokus


def sibenice():
    '''Hraje sibenici. '''

    slovo = vyber_slovo()
    neuspesny_pokus = 0
    pole = '_' * len(slovo)
    while True:
        print('Hraci pole:', pole)
        pole, neuspesny_pokus = tah(pole, slovo, neuspesny_pokus)
        print('Pocet neuspesnych pokusu:', neuspesny_pokus)
        if vyhodnot(pole, neuspesny_pokus) != '-':
            break


sibenice()
