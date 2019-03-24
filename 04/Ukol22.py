import sys
# Ukol 22

print('Ukol 22')

n = int(input('Zadej cislo pro vypocet faktorialu, potvrzeni prvocisla a vypis'
        ' Fibonacciho posloupnosti: '))

# vylouci zaporna cisla
if n < 0:
    print('Zadej pouze kladne cislo nebo 0.')
    sys.exit()


# vypocte faktorial

faktorial = 1

for cislo in range(1, n + 1):
    faktorial = cislo * faktorial
print('Faktorial ', n, '! je ', faktorial, '.')

# zjisti zda je n prvocislo
je_prvocislo = True
for cislo2 in range(n - 1, 1, -1):
    if n % cislo2 == 0:
        je_prvocislo = False
        break
if je_prvocislo:
    print(n, ' je prvocislo.')
else:
    print(n, 'neni prvocislo.')

# vypise prvnich n clenu Fibonacciho posloupnosti

# prvni 2 cisla posloupnosti
n0 = 0
n1 = 1
suma = 1

print('Fibonacciho posloupnost ', n, 'je')

for index in range(1, n + 1):
    print(index, '. ', suma)
    suma = n0 + n1

    # zaktualizuje hodnoty pro dalsi krok
    n0 = n1
    n1 = suma
