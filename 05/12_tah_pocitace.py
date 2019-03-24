from random import randrange

symbol_pocitace = 'x'


def tah_pocitace(pole):
    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """
    while True:
        cislo_policka = randrange(0, 20)
        print(cislo_policka)

        if pole[cislo_policka] == '-':
            return pole[:cislo_policka] + symbol_pocitace + pole[cislo_policka + 1:]


print(tah_pocitace('--------------------'))
