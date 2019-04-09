from random import randrange
from util import tah


def tah_pocitace(pole, symbol_pocitace, symbol_hrace, delka_pole):
    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """

    while True:
        if delka_pole == 0:
            raise ValueError('Nulove pole. To si moc nezahrajes.')
        if delka_pole < 6:
            raise ValueError('Na poli mensim 6 policek nejde hrat.')
        if '-' not in pole:
            raise ValueError('Pole je zaplneno.')

        cislo_policka = randrange(0, delka_pole)
        if (symbol_pocitace + '-' + symbol_pocitace) in pole:
            cislo_policka = pole.index(symbol_pocitace + '-' + symbol_pocitace) + 1
            print('Pocitac hraje na pozici: ', cislo_policka + 1)
            return tah(pole, cislo_policka, symbol_pocitace)
        elif (symbol_hrace + '-') in pole:
            cislo_policka = pole.index(symbol_hrace + '-') + 1
            print('Pocitac hraje na pozici: ', cislo_policka + 1)
            return tah(pole, cislo_policka, symbol_pocitace)
        elif ('-' + symbol_hrace) in pole:
            cislo_policka = pole.index('-' + symbol_hrace)
            print('Pocitac hraje na pozici: ', cislo_policka + 1)
            return tah(pole, cislo_policka, symbol_pocitace)
        elif ('-' * delka_pole) in pole:
            cislo_policka = pole.index('---')
            print('Pocitac hraje na pozici: ', cislo_policka + 1)
            return tah(pole, cislo_policka, symbol_pocitace)
