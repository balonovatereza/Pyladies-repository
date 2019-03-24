def tah_hrace(pole):
    """
    Zeptá se hráče, kam chce hrát, a vrátí herní pole s jeho zaznamenaným
    tahem.
    """

    while True:
        cislo_policka = int(input('Zadej cislo policka 0-19, na ktere chces'
                                  'vlozit \'o\': '))
        if 0 <= cislo_policka <= 19:
            if pole[cislo_policka] == '-':
                print(pole[cislo_policka])
                return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
            else:
                print('Nemuzes zahrat na uz obsazene pole.')
        else:
            print('Zadal jsi cislo mimo rozsah hraciho pole.')


print(tah_hrace('--------------------'))
