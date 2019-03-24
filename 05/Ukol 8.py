from random import randrange


def hod_kostkou(cislo_hrace):
    '''Vraci pocet potrebnych hodu'''
    cislo = 0
    pocet_hodu = 0
    print('hrac ', cislo_hrace)
    while cislo != 6:
        cislo = randrange(1, 7)
        pocet_hodu += 1
        print(cislo)

    print('Pocet hodu: ', pocet_hodu)

    return pocet_hodu


cislo_hrace = 1
nejvyssi_pocet_hodu = 0

for i in range(1, 5):
    pocet_hodu = hod_kostkou(i)

    if pocet_hodu > nejvyssi_pocet_hodu:
        nejvyssi_pocet_hodu = pocet_hodu
        cislo_hrace = i

print('Vyhral hrac cislo: ', cislo_hrace)
