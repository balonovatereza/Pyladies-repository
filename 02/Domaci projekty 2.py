# Ukol 6: Program spocita povrch a objem krychle o strane 2852cm.

strana = 2852  # v cm
povrch = 6 * strana**2
objem = strana**3

print('Povrch krychle o strane ', strana, ' je ', povrch, ' cm2 a jeji objem je ', objem, ' cm3.')


# Ukol 7:

strana2 = float(input('Zadej delku strany krychle, a ja spocitam povrch a objem:'))
povrch2 = 6 * strana2**2
objem2 = strana2**3

print('Povrch krychle o strane ', strana2, ' je ', povrch2, ' cm2 a jeji objem je ', objem2, ' cm3.')

# Ukol 9
from random import randrange
cislo = randrange(3)
print(cislo)

if cislo == 1:
    tah_pocitace = 'nůžky'
elif cislo == 0:
    tah_pocitace = 'kámen'
else:
    tah_pocitace = 'papír'

tah_cloveka = input('kámen, nůžky, nebo papír? ')

if tah_cloveka == 'kámen':
    if tah_pocitace == 'kámen':
        print('Plichta.')
    elif tah_pocitace == 'nůžky':
        print('Vyhrála jsi!')
    elif tah_pocitace == 'papír':
        print('Počítač vyhrál.')
elif tah_cloveka == 'nůžky':
    if tah_pocitace == 'kámen':
        print('Počítač vyhrál.')
    elif tah_pocitace == 'nůžky':
        print('Plichta.')
    elif tah_pocitace == 'papír':
        print('Vyhrála jsi!')
elif tah_cloveka == 'papír':
    if tah_pocitace == 'kámen':
        print('Vyhrála jsi!')
    elif tah_pocitace == 'nůžky':
        print('Počítač vyhrál.')
    elif tah_pocitace == 'papír':
        print('Plichta.')
else:
    print('Nerozumím.')

# Ukol 13

pocet_tykadel = int(input('Kolik mas tykadel '))
if pocet_tykadel >= 3:
    print('Tykadla jsou parovy organ, nespletl ses?')
elif pocet_tykadel == 2:
    print('Mas dve tykadla')
elif pocet_tykadel == 1:
    print('Zbylo ti jedno tykadlo')
elif pocet_tykadel == 0:
    print('Nemas tykadla')
else:
    # Nenastala ani nedna ze situací výše – muselo to být záporné nebo necele cislo
    print('Beru jen cela tykadla, zaporna tykadla taky neberu, zkus to znovu.')

# Ukol 14

tajneHeslo = 'Abrakadabra'
tipUzivatele = input('Zadej tajne heslo: ')

if tipUzivatele == 'Abrakadabra':
    print('V patek jsem videla cerneho havrana.')
else:
    print('Spatne heslo, zkus to znova.')

# Ukol 17

from random import randrange
cislo = randrange(3)
print(cislo)

if cislo == 1:
    tah_pocitace = 'nůžky'
elif cislo == 0:
    tah_pocitace = 'kámen'
else:
    tah_pocitace = 'papír'

tah_cloveka = input('kámen, nůžky, nebo papír? ')

if (tah_cloveka == 'kámen' and tah_pocitace == 'kámen') or (tah_cloveka == 'nůžky' and tah_pocitace == 'nůžky') or (tah_cloveka == 'papír' and tah_pocitace == 'papír'):
    print('Plichta.')
elif (tah_cloveka == 'nůžky' and tah_pocitace == 'kámen') or (tah_cloveka == 'papír' and tah_pocitace == 'nůžky') or (tah_cloveka == 'kámen' and tah_pocitace == 'papír'):
    print('Počítač vyhrál.')
elif (tah_cloveka == 'kámen' and tah_pocitace == 'nůžky') or (tah_cloveka == 'nůžky' and tah_pocitace == 'papír') or (tah_cloveka == 'papír' and tah_pocitace == 'kámen'):
    print('Vyhrála jsi!')
else:
    print('Nerozumím.')


# Ukol 18
# Tento program rozdává naivní rady do života.

print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')
if stastna_retezec == 'ano':
    stastna = True
elif stastna_retezec == 'ne':
    stastna = False
else:
    print('Nerozumím!')

bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano':
    bohata = True
elif bohata_retezec == 'ne':
    bohata = False
else:
    print('Nerozumím!')

if bohata:
    if stastna:
        # Je bohatá a zároveň štǎstná, ta se má.
        print('Gratuluji!')
    else:
        # Je bohatá, ale není „bohatá a zároveň šťastná“,
        # takže musí být jen bohatá.
        print('Zkus se víc usmívat.')

else:
    if stastna:
        # Tady musí být jen šťastná.
        print('Zkus míň utrácet.')
    else:
        # A tady víme, že není ani šťastná, ani bohatá.
        print('To je mi líto.')
