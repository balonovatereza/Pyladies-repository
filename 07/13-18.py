from random import randrange


def nakresli_mapu(velikost, potrava, had, tajemna_potrava):
    seznam_radku = []
    for y in range(velikost):
        radek = []
        for x in range(velikost):
            if (x, y) in potrava:
                radek.append('X')
            elif (x, y) in had:
                radek.append('X')
            elif (x, y) in tajemna_potrava:
                radek.append('?')
            else:
                radek.append('.')
        seznam_radku.append(radek)
    return seznam_radku


def vygeneruj_potravu(velikost_pole, had, potrava, tajemna_potrava):
    while True:
        x = randrange(velikost_pole)
        y = randrange(velikost_pole)
        if (x, y) not in had and (x, y) not in potrava and (x, y) not in tajemna_potrava:
            print(x, y)
            return (x, y)


def pohyb(velikost_pole, had, svetova_strana, potrava):
    x, y = had[-1]
    if svetova_strana == 's':
        novy_krok = x, y-1
    elif svetova_strana == 'j':
        novy_krok = x, y+1
    elif svetova_strana == 'v':
        novy_krok = x+1, y
    elif svetova_strana == 'z':
        novy_krok = x-1, y

    if novy_krok in had:
        raise ValueError('Game over. Narazil jsi do sebe.')

    x, y = novy_krok
    if x > (velikost_pole-1) or x < 0 or y > (velikost_pole-1) or y < 0:
        raise ValueError('Game over. Narazil jsi do steny.')

    if novy_krok not in potrava:
        del had[0]
    else:
        del potrava[0]
        potrava.append(vygeneruj_potravu(velikost_pole, had, potrava, tajemna_potrava))
    had.append(novy_krok)
    print(had)


had = [(0, 0), (1, 0), (2, 0)]
potrava = [(2, 3)]
tajemna_potrava = []


def zadej_velikost_pole():
    while True:
        velikost_pole = input('Zadej velikost hraciho pole (vetsi nez 4): ')
        if not velikost_pole.isdigit():
            print('Muzes zadat jen celociselny kladny vstup.')
            continue
        velikost_pole = int(velikost_pole)
        if velikost_pole <= 4:
            print('Nelze hrat na poli mensim 5. Zadej vetsi rozmer pole.')
        else:
            return velikost_pole


counter = 0
velikost_pole = zadej_velikost_pole()
while True:
    mapa = nakresli_mapu(velikost_pole, potrava, had, tajemna_potrava)
    for radek in mapa:
        for znak in radek:
            print(znak, end=' ')
        print()
    counter = counter + 1
    if counter % 30 == 0:
        tajemna_potrava.append(vygeneruj_potravu(velikost_pole, had, potrava, tajemna_potrava))
    svetova_strana = input('Zadej smer pohybu (s, j, v, z): ').lower().strip()
    if svetova_strana not in ('s', 'j', 'v', 'z'):
        print('Takovy smer neznam, zadej pouze s, j, v nebo z: ')
    else:
        pohyb(velikost_pole, had, svetova_strana, potrava)
print(had)
