from random import randrange


def nakresli_mapu(vyska, sirka, potrava, had, tajemna_potrava):
    seznam_radku = []
    for y in range(vyska):
        radek = []
        for x in range(sirka):
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


def vygeneruj_potravu(vyska, sirka, had, potrava, tajemna_potrava):
    while True:
        x = randrange(sirka)
        y = randrange(vyska)
        if (x, y) not in had and (x, y) not in potrava and (x, y) not in tajemna_potrava:
            print(x, y)
            return (x, y)


def pohyb(vyska, sirka, had, svetova_strana, potrava):
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
    if x > (sirka-1) or x < 0 or y > (vyska-1) or y < 0:
        raise ValueError('Game over. Narazil jsi do steny.')

    if novy_krok not in potrava:
        del had[0]
    else:
        del potrava[0]
        potrava.append(vygeneruj_potravu(vyska, sirka, had, potrava, tajemna_potrava))
    had.append(novy_krok)
    print(had)


had = [(0, 0), (1, 0), (2, 0)]
potrava = [(2, 1)]
tajemna_potrava = []


def zadej_velikost_pole():
    while True:
        vyska = input('Zadej vysku hraciho pole: ')
        sirka = input('Zadej sirku hraciho pole: ')
        if not vyska.isdigit() or not sirka.isdigit():
            print('Muzes zadat jen celociselny kladny vstup.')
            continue
        vyska, sirka = int(vyska), int(sirka)
        if vyska < 2:
            print('Pole musi mit minimalne 2 radky. Zadej vetsi rozmer pole.')
        elif sirka < 5:
            print('Minimalni sirka pole je 5. Zadej vesti rozmer pole.')
        else:
            return vyska, sirka


counter = 0
vyska, sirka = zadej_velikost_pole()
while True:
    mapa = nakresli_mapu(vyska, sirka, potrava, had, tajemna_potrava)
    for radek in mapa:
        for znak in radek:
            print(znak, end=' ')
        print()
    counter = counter + 1
    if counter % 30 == 0:
        tajemna_potrava.append(vygeneruj_potravu(vyska, sirka, had, potrava, tajemna_potrava))
    svetova_strana = input('Zadej smer pohybu (s, j, v, z): ').lower().strip()
    if svetova_strana not in ('s', 'j', 'v', 'z'):
        print('Takovy smer neznam, zadej pouze s, j, v nebo z: ')
    else:
        pohyb(vyska, sirka, had, svetova_strana, potrava)
print(had)
