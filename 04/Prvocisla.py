n = int(input('Zadej cislo, u ktereho chces zjistit zda je prvocislo: '))

je_prvocislo = True
for index in range(n - 1, 1, -1):
    if n % index == 0:
        je_prvocislo = False
        break
if je_prvocislo:
    print(n, ' je prvocislo.')
else:
    print(n, 'neni prvocislo.')
