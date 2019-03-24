cisla = [1, 1, 2, 3, 5, 8, 13]
print(cisla)  # vypise seznam na jeden radek, tak jak je zapsany vyse

for cislo in cisla:
    print(cislo)  # vypise kazdou polozku na novy radek

seznam = [1, 'abc', True, None, range(10), len]
print(seznam)

print(cisla[2])
print(cisla[2:-3])

prvocisla = [2, 3, 5, 7, 11, 13, 17]
print(prvocisla)
prvocisla.append(19)  # existuje metoda insert, ktere reknes kam to v tom seznamu chces dat
print(prvocisla)

a = [1, 2, 3]   # vytvoření seznamu
b = a           # tady se nový seznam nevytváří

# seznam vytvořený v prvním řádku má teď dvě jména: "a" a "b",
# ale stále pracujeme jenom s jedním seznamem

print(b)
a.append(4)  # vlozi do seznamu jeden prvek
print(b)

dalsi_prvocisla = [23, 29, 31]
prvocisla.extend(dalsi_prvocisla)
print(prvocisla)

seznam = []
seznam.extend('abcdef')  # vlozi do seznamu vice prvku
seznam.extend(range(10))
print(seznam)

cisla = [1, 0, 3, 4]
cisla[1] = 2
print(cisla)

cisla = [1, 2, 3, 4]
cisla[1:-1] = [6, 5]
print(cisla)

cisla = [1, 2, 3, 4]
cisla[1:-1] = [0, 0, 0, 0, 0, 0]
print(cisla)
cisla[1:-1] = []
print(cisla)

cisla = [1, 2, 3, 4, 5, 6]
del cisla[-1]
print(cisla)
del cisla[3:5]
print(cisla)
del cisla
# print(cisla) vyhodi chybu name error, protoze seznam cisla uz neexistuje

cisla = [1, 2, 3, 'abc', 4, 5, 6, 12]
posledni = cisla.pop()
print(posledni)
print(cisla)

cisla.remove('abc')
print(cisla)

cisla.clear()
print(cisla)

seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
seznam.sort()
print(seznam)

seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
seznam.sort(reverse=True)
print(seznam)

melodie = ['C', 'E', 'G'] * 2 + ['E', 'E', 'D', 'E', 'F', 'D'] * 2 + ['E', 'D', 'C']
print(melodie)

print(len(melodie))         # Délka seznamu
print(melodie.count('D'))   # Počet 'D' v seznamu
print(melodie.index('D'))   # Číslo prvního 'D'
print('D' in melodie)       # Je 'D' v seznamu?
print('DE' in melodie)
print(melodie.count('DE'))
# print(melodie.index('DE')) vypise valueerror, de is not in the list

if seznam:
    print('V seznamu něco je!')
else:
    print('Seznam je prázdný!')

abeceda = list('abcdefghijklmnopqrstuvwxyz')
cisla = list(range(100))
print(abeceda)
print(cisla)

a = [1, 2, 3]
b = list(a)

print(b)
a.append(4)
print(b)

mocniny_dvou = []
for cislo in range(10):
    mocniny_dvou.append(2 ** cislo)
print(mocniny_dvou)

balicek = []
for barva in '♠', '♥', '♦', '♣':  # (Na Windows použij textová jména)
    for hodnota in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        balicek.append(str(hodnota) + barva)
print(balicek)

slova = 'Tato věta je složitá, rozdělme ji na slova!'.split()
print(slova)

zaznamy = '3A,8B,2E,9D'.split(',')
print(zaznamy)

veta = ' '.join(slova)
print(veta)


def vytvor_tabulku(velikost=11):
    seznam_radku = []
    for a in range(velikost):
        radek = []
        for b in range(velikost):
            radek.append(a * b)
        seznam_radku.append(radek)
    return seznam_radku


nasobilka = vytvor_tabulku()

print(nasobilka[2][3])  # dva krát tři
print(nasobilka[5][2])  # pět krát dva
print(nasobilka[8][7])  # osm krát sedm

# Vypsání celé tabulky
for radek in nasobilka:
    for cislo in radek:
        print(cislo, end=' ')
    print()
