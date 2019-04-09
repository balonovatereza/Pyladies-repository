from ai import tah_pocitace
from util import tah


def vyhodnot(pole, symbol_hrace, symbol_pocitace):
    """
    Podle stavu herního pole vrátí:
     řetězec "x", když vyhraje hráč,
     řetězec "o", když vyhraje počítač,
     řetězec "!", když dojde k remíze nebo
     řetězec "-", když je možné ještě pokračovat ve hře
    """
    if 3 * symbol_hrace in pole:
        return symbol_hrace
    elif 3 * symbol_pocitace in pole:
        return symbol_pocitace
    elif '-' not in pole:
        return '!'
    else:
        return '-'


def tah_hrace(pole, symbol_hrace, delka_pole):
    """
    Zeptá se hráče, kam chce hrát, a vrátí herní pole s jeho zaznamenaným
    tahem.
    """

    while True:
        try:
            cislo_policka = int(input('Zadej cislo policka 1-' + str(delka_pole) + ' na ktere chces'
                                      ' vlozit \'' + symbol_hrace + '\': '))

        except ValueError:
            print('Muzes zadat pouze cislo, zkus to znovu.')
        else:
            if 1 <= cislo_policka <= delka_pole:
                if pole[cislo_policka - 1] == '-':
                    return tah(pole, cislo_policka - 1, symbol_hrace)
                else:
                    print('Nemuzes zahrat na uz obsazene pole.')
            else:
                print('Zadal jsi cislo mimo rozsah hraciho pole.')


def piskvorky1d():
    """
    Hraje 1D piškvorky.
    """

    delka_pole = 21
    symbol_hrace = 'x'
    symbol_pocitace = 'o'
    pole = delka_pole * '-'
    stav_hry = '-'
    hraje_pocitac = False
    while stav_hry == '-':
        if hraje_pocitac:
            pole = tah_pocitace(pole, symbol_pocitace, symbol_hrace, delka_pole)
        else:
            pole = tah_hrace(pole, symbol_hrace, delka_pole)
        print(pole)
        stav_hry = vyhodnot(pole, symbol_hrace, symbol_pocitace)
        hraje_pocitac = not hraje_pocitac

    if stav_hry == symbol_hrace:
        print('Vyhral jsi!')
    elif stav_hry == symbol_pocitace:
        print('Vyhral pocitac!')
    elif stav_hry == '!':
        print('Remiza')
    return symbol_hrace, symbol_pocitace, delka_pole
