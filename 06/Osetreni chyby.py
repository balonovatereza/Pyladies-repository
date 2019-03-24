def nacti_cislo():
    odpoved = input('Zadej číslo: ')
    try:
        cislo = int(odpoved)
    except ValueError:
        print('To nebylo číslo! Pokračuji s nulou.')
        cislo = 0
    return cislo
