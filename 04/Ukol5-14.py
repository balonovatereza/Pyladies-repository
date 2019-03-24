# Ukol 5

print('Ukol 5')
pocet_radku = int(input('Zadej pocet radku: '))
for i in range(pocet_radku):
    print('a', sep='')

# Ukol 6

print('Ukol 6')
pocet_radku2 = int(input('Zadej pocet radku: '))
for cislo_radku in range(pocet_radku2):
    print('Radek ', cislo_radku)

# Ukol 8

print('Ukol 8')
pocet = int(input('Zadej nejvyssi cislo, na kterem skoncim mocnit: '))
for mocnenec in range(pocet):
    print(mocnenec, ' na druhou je ', mocnenec**2)

# Ukol 9
print('Ukol 9 - reseni ternarnim operatorem')
for i in range(1, 26):
    oddelovac = ' ' if (i % 5) != 0 else '\n'
    print('X', end=oddelovac)

print('Ukol 9 - reseni pomoci 2 cyklu for vnorenych do sebe')

sirka = int(input('Zadej sirku tabulky: '))
for terminator in range(sirka):
    for sloupecek in range(sirka - 1):
        print('X', end=' ')
    print('X', end='\n')

#  reseni ukolu 9 z hodiny
for j in range(5):
    print('X ' * 5)

# Ukol 10

print('Ukol 10')
sirka_nasobilky = int(input('Zadej sirku tabulky: '))
for cinitel_a in range(sirka_nasobilky):
    for cinitel_b in range(sirka_nasobilky - 1):
        print(cinitel_a * cinitel_b, end=' ')
    print(cinitel_a * (cinitel_b + 1), end='\n')

# Ukol 11

print('Ukol 11')

velikost_trojuhelniku = int(input('Zadej velikost trojuhelniku: '))
for i in range(velikost_trojuhelniku):
    for j in range(i):
        print('X', end=' ')
    print('X', end='\n')

#  reseni Ukolu 11 z hodiny
for radek in range(1, 5):
    print('X ' * radek)

# Ukol 12

print('Ukol 12')
pocet_radku_tabulky = int(input('Zadej pocet radku: '))
for cisloRadku in range(1, pocet_radku_tabulky):
    if cisloRadku == 1:
        print('prvni radek')
    else:
        print('neni prvni')

# Ukol 13

print('Ukol 13')

sirka_ctverce = int(input('Zadej sirku ctverce: '))

for osa_X in range(sirka_ctverce):
    for osa_Y in range(sirka_ctverce):
        znak = ' '
        konec = ' '
        if osa_X == 0 or osa_X == (sirka_ctverce - 1) or osa_Y == 0 or \
                osa_Y == (sirka_ctverce - 1):
            znak = 'X'
        if osa_Y == (sirka_ctverce - 1):
            konec = '\n'
        print(znak, end=konec)
