from random import randrange

tah_cloveka = ''
while tah_cloveka != 'konec':
    tah_cloveka = input('kámen, nůžky, nebo papír? Pokud chces skoncit, zadej konec.')

    if tah_cloveka == 'konec':
        break

    cislo = randrange(3)

    if cislo == 1:
        tah_pocitace = 'nůžky'
    elif cislo == 0:
        tah_pocitace = 'kámen'
    else:
        tah_pocitace = 'papír'
    print(tah_pocitace)

    if tah_cloveka == tah_pocitace:
        print('Plichta.')
    elif tah_cloveka == 'kámen' and tah_pocitace == 'nůžky' or \
            tah_cloveka == 'nůžky'and tah_pocitace == 'papír' or \
            tah_cloveka == 'papír' and tah_pocitace == 'kámen':
        print('Vyhrála jsi!')
    else:
        print('Počítač vyhrál.')
