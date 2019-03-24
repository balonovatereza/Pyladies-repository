
mensiCislo = None

for i in range(5):
    zadaneCislo = float(input('Zadej cislo:'))
    mensiCislo = mensiCislo if mensiCislo is not None and mensiCislo < zadaneCislo else zadaneCislo

print(mensiCislo)
