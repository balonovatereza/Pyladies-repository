# Ukol 19

print('Ukol 19')

suma = 0
for cislo in range(3):
    cislo = int(input('Zadej cislo:'))
    suma = suma + cislo

if suma > 10:
    print('Soucet tvych cisel je: ', suma, ' a to je vetsi nez 10.')
else:
    print('Soucet tvych cisel je: ', suma, ' a to rozhodne vetsi nez 10 neni.')

# Ukol 20

print('Ukol 20')

sude_liche = int(input('Zadej cislo:'))

if sude_liche % 2 == 0:
    print('Cislo ', sude_liche, ' je sude.')
else:
    print('Cislo ', sude_liche, ' je liche.')

# Ukol 21

print('Ukol 21')
cislo_delitelne_3 = 'bum'
cislo_delitelne_5 = 'bac'
cislo_delitelne_3i5 = 'bum-bac'

for numero in range(101):
    if numero % 3 == 0 and numero % 5 == 0:
        numero = cislo_delitelne_3i5
    elif numero % 3 == 0:
        numero = cislo_delitelne_3
    elif numero % 5 == 0:
        numero = cislo_delitelne_5
    print(numero)

# Ukol 22

print('Ukol 22')

faktorial = 1
n = int(input('Zadej cislo pro vypocet faktorialu: '))

for cislo in range(1, n + 1):
    faktorial = cislo * faktorial
print(faktorial)
