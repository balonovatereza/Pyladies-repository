from random import randrange

DELKA_POLE = 20

SYMBOL_HRACE = 'x'
SYMBOL_POCITACE = 'o'


def vyhodnot(pole):
    """
    Podle stavu herního pole vrátí:
     řetězec "x", když vyhraje hráč,
     řetězec "o", když vyhraje počítač,
     řetězec "!", když dojde k remíze nebo
     řetězec "-", když je možné ještě pokračovat ve hře
    """
    if 3 * SYMBOL_HRACE in pole:
        return SYMBOL_HRACE
    elif 3 * SYMBOL_POCITACE in pole:
        return SYMBOL_POCITACE
    elif '-' not in pole:
        return '!'
    else:
        return '-'


def tah(pole, cislo_policka, symbol):
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici.
    """
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]


def tah_hrace(pole):
    """
    Zeptá se hráče, kam chce hrát, a vrátí herní pole s jeho zaznamenaným
    tahem.
    """

    while True:
        try:
            cislo_policka = int(input('Zadej cislo policka 1-' + str(DELKA_POLE) + ', na'
                                      ' ktere chces vlozit \'' + SYMBOL_HRACE + '\': '))

        except ValueError:
            print('Muzes zadat pouze cislo, zkus to znovu.')
        else:
            if 1 <= cislo_policka <= DELKA_POLE:
                if pole[cislo_policka - 1] == '-':
                    return tah(pole, cislo_policka - 1, SYMBOL_HRACE)
                else:
                    print('Nemuzes zahrat na uz obsazene pole.')
            else:
                print('Zadal jsi cislo mimo rozsah hraciho pole.')


def tah_pocitace(pole):
    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """

    while True:
        cislo_policka = randrange(0, 20)

        if (SYMBOL_POCITACE + '-' + SYMBOL_POCITACE) in pole:
            cislo_policka = pole.index(SYMBOL_POCITACE + '-' + SYMBOL_POCITACE) + 1
            print('Pocitac hraje na pozici: ', cislo_policka + 1)
            return tah(pole, cislo_policka, SYMBOL_POCITACE)
        elif (SYMBOL_HRACE + '-') in pole:
            cislo_policka = pole.index(SYMBOL_HRACE + '-') + 1
            print('Pocitac hraje na pozici: ', cislo_policka + 1)
            return tah(pole, cislo_policka, SYMBOL_POCITACE)
        elif ('-' + SYMBOL_HRACE) in pole:
            cislo_policka = pole.index('-' + SYMBOL_HRACE)
            print('Pocitac hraje na pozici: ', cislo_policka + 1)
            return tah(pole, cislo_policka, SYMBOL_POCITACE)


def piskvorky1d():
    """
    Hraje 1D piškvorky.
    """

    pole = DELKA_POLE * '-'
    stav_hry = '-'
    hraje_pocitac = False
    while stav_hry == '-':
        if hraje_pocitac:
            pole = tah_pocitace(pole)
        else:
            pole = tah_hrace(pole)
        print(pole)
        stav_hry = vyhodnot(pole)
        hraje_pocitac = not hraje_pocitac

    if stav_hry == SYMBOL_HRACE:
        print('Vyhral jsi!')
    elif stav_hry == SYMBOL_POCITACE:
        print('Vyhral pocitac!')
    elif stav_hry == '!':
        print('Remiza')


if __name__ == "__main__":
    piskvorky1d()
