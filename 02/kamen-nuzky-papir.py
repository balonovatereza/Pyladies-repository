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
