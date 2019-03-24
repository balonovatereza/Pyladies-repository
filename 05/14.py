from random import randrange
DELKA_POLE = 20
pole = '-oo-----------------'
SYMBOL_HRACE = 'x'
SYMBOL_POCITACE = 'o'

cislo_policka = randrange(0, DELKA_POLE)
print('Pocitac hraje na pozici: ', cislo_policka)
print(pole.index(SYMBOL_POCITACE + SYMBOL_POCITACE + '-'))

# elif SYMBOL_HRACE + '-' in pole and pole[cislo_policka] == '-':
# return tah(pole, cislo_policka, SYMBOL_POCITACE)

        if (SYMBOL_POCITACE + SYMBOL_POCITACE + '-') in pole:
            cislo_policka = pole.index(SYMBOL_POCITACE + SYMBOL_POCITACE + '-') + 2
            return tah(pole, cislo_policka, SYMBOL_POCITACE)
        elif ('-' + SYMBOL_POCITACE + SYMBOL_POCITACE) in pole:
            cislo_policka = pole.index('-' + SYMBOL_POCITACE + SYMBOL_POCITACE)
            return tah(pole, cislo_policka, SYMBOL_POCITACE)
        elif (SYMBOL_HRACE + '-') in pole:
            cislo_policka = pole.index(SYMBOL_HRACE + '-')
            return tah(pole, cislo_policka, SYMBOL_POCITACE)
        elif ('-' + SYMBOL_HRACE) in pole:
            cislo_policka = pole.index('-' + SYMBOL_HRACE)
            return tah(pole, cislo_policka, SYMBOL_POCITACE)
