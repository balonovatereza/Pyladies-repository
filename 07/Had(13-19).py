from random import randrange


def nakresli_mapu(vyska, sirka, potrava, had, tajemna_potrava):
    '''
    Na vysku a sirku vygeneruje a vrati seznam radku hraciho pole.
    '''
    for y in range(vyska):
        for x in range(sirka):
            if (x, y) in potrava:
                print('o', end=' ')
            elif (x, y) in had:
                print('x', end=' ')
            elif (x, y) in tajemna_potrava:
                print('?', end=' ')
            else:
                print('.', end=' ')
        print()


def vygeneruj_potravu(vyska, sirka, had, potrava, tajemna_potrava):
    '''
    Nahodne vygeneruje souradnice potravy, proveri, zda nejsou v seznamu
    hada, potravy nebo tajemne potravy a vrati tyto souradnice.
    '''
    while True:
        x = randrange(sirka)
        y = randrange(vyska)
        if (x, y) not in had and (x, y) not in potrava and (x, y) not in tajemna_potrava:
            return (x, y)


def pohyb(vyska, sirka, had, svetova_strana, potrava):
    '''
    Vezme posledni souradnice hada(hlavu) a podle smeru pohybu spocita novy krok,
    proveri, zda souradnice noveho kroku nejsou v seznamu hada nebo mimo hraci pole,
    proveri, zda novy krok neni v seznamu potravy, pokud ano, umaze potravu
    a vygeneruje novou, pokud ne, umaze hadovi konec ocasu.

    '''
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


had = [(0, 0), (1, 0), (2, 0)]
potrava = [(2, 1)]
tajemna_potrava = []


def zadej_velikost_pole():
    '''
    Vyzyva hrace k zadani vysky a sirky hraciho pole, proveri, zda se jedna
    o celociselne hodnoty, zda je hraci pole vetsi 4x1 a vrati vysku a sirku.
    '''
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


counter = 0  # pocitadlo tahu
vyska, sirka = zadej_velikost_pole()
x, y = had[-1]
while True:
    mapa = nakresli_mapu(vyska, sirka, potrava, had, tajemna_potrava)
    counter = counter + 1
    if counter % 30 == 0:
        tajemna_potrava.append(vygeneruj_potravu(vyska, sirka, had, potrava, tajemna_potrava))
    svetova_strana = input('Zadej smer pohybu (s, j, v, z): ').lower().strip()
    if svetova_strana not in ('s', 'j', 'v', 'z'):
        print('Takovy smer neznam, zadej pouze s, j, v nebo z: ')
    else:
        pohyb(vyska, sirka, had, svetova_strana, potrava)
