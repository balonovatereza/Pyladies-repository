import random


def kresli_obesence(neuspesny_pokus):
    '''
    Na zaklade neuspesnych pokusu vypise obrazek obesence.
    '''

    with open(str(neuspesny_pokus) + '.txt', encoding='utf-8') as soubor:
        print(soubor.read())


def vyhodnot(pole, neuspesny_pokus):
    '''
    Podle poctu neuspesnych pokusu a stavu herniho pole vrati:
    '-' - pokud hra dale pokracuje
    '!' - pokud hra konci (hrac vyhral nebo prohral)
    '''

    if neuspesny_pokus == 10:
        print('Konec hry, prohral jsi.')
        return '!'
    elif '_' not in pole:
        print('Vyhral jsi.')
        return '!'
    else:
        return '-'


def vyber_slovo():
    '''
    Ze zadanych slov nahodne vybere slovo.
    '''

    slova = ['smudla', 'profa', 'kejchal', 'rejpal', 'stydlin', 'stistko',
             'drimal', 'snehurka']
    slovo = random.choice(slova)
    print(slovo)
    return slovo


def zadej_pismeno(pole):
    '''
    Vyzve hrace k zadani pismena a zkontroluje, jestli je to jen jeden
    znak, pismeno abecedy a jestli se nejedna o pismeno zadane opakovane.
    '''

    while True:
        pismeno = input('Hadej pismeno: ').strip().lower()
        if len(pismeno) > 1 or len(pismeno) < 1:
            print('Muzes zadat jen jedno pismeno.')
        elif not pismeno.isalpha():
            print('Muzes zadat jen pismena abecedy.')
        elif pismeno in pole:
            print('Toto pismeno uz jsi zadal.')
        else:
            return pismeno


def nahrad_znaky(pole, slovo, pismeno):
    '''
    Prochazi postupne znaky hadaneho slova, porovnava s hadanym pismenem,
    pokud najde shodu, znak vepise do pole a vrati pole.
    '''

    for i in range(len(slovo)):
        if slovo[i] == pismeno:
            pole = pole[:i] + pismeno + pole[i + 1:]
    return pole


def tah(pole, slovo, neuspesny_pokus):
    '''
    Vezme zadane pismeno a vrati herni pole se zaznamenanym tahem
     a upraveny pocet neuspesnych pokusu.
    '''

    pismeno = zadej_pismeno(pole)

    if pismeno in slovo:
        pole = nahrad_znaky(pole, slovo, pismeno)
        return pole, neuspesny_pokus
    elif pismeno not in slovo:
        neuspesny_pokus += 1
        kresli_obesence(neuspesny_pokus)
        return pole, neuspesny_pokus


def sibenice():
    '''
    Hraje sibenici.
    '''

    slovo = vyber_slovo()
    neuspesny_pokus = 0
    pole = '_' * len(slovo)
    while True:
        print('Hraci pole:', pole)
        pole, neuspesny_pokus = tah(pole, slovo, neuspesny_pokus)
        print('Pocet neuspesnych pokusu:', neuspesny_pokus)
        if vyhodnot(pole, neuspesny_pokus) != '-':
            break


while True:
    sibenice()
    otazka = input('Chces hrat znovu (ano/ne)? ')
    if otazka.strip().lower() != 'ano':
        print('Nashledanou.')
        break
