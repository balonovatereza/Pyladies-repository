def vytvor_slovnik_mocnin(n):
    '''
    Vytvori a vrati slovnik druhych mocnin az po cislo n.
    '''
    slovnik_mocnin = {}
    for cislo in range(1, n + 1):
        slovnik_mocnin[cislo] = cislo**2
    return slovnik_mocnin


n = int(input('Zadej cislo a ja vytvorim slovnik s mocninami: '))


def vypis_slovnik(slovnik):
    for klic, hodnota in slovnik.items():
        print('Klic {}: hodnota {}'.format(klic, hodnota))


vypis_slovnik(vytvor_slovnik_mocnin(n))
