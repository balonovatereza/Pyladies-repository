from random import randrange

soucet = 0
while soucet <= 21:
    print('Nasbiral jsi ', soucet, ' bodu')
    dalsiKartu = input('Chces dalsi kartu?')
    if dalsiKartu == 'Ano':
        dalsiKarta = randrange(2, 11)
        soucet = soucet + dalsiKarta
        print('Na karte mas: ', dalsiKarta, ' bodu.')
    elif dalsiKartu == 'Ne':
        print('Konec hry')
        break
    else:
        print('Nerozumim, zkus to znovu.')

if soucet == 21:
    print('Vyhral jsi!')
elif soucet < 21:
    print('Mas ', soucet, 'bodu.')
elif soucet > 21:
    print('Too much bodu, mas ', soucet, 'bodu.')
