def vytvor_slovnik_mocnin(n):
    '''
    Vytvori a vrati slovnik druhych mocnin az po cislo n.
    '''
    slovnik_mocnin = {}
    for cislo in range(1, n + 1):
        slovnik_mocnin[cislo] = cislo**2
    return slovnik_mocnin


n = int(input('Zadej cislo a ja vytvorim slovnik s mocninami: '))


def vrat_sumu_klicu_a_hodnot(slovnik):
    '''
    Vrati sumu vsech klicu a hodnot z argumentem zadaneho slovniku.
    '''
    suma_klicu = 0
    suma_hodnot = 0
    for klic, hodnota in slovnik.items():
        suma_klicu += klic
        suma_hodnot += hodnota
    return suma_klicu, suma_hodnot


print(vrat_sumu_klicu_a_hodnot(vytvor_slovnik_mocnin(n)))
