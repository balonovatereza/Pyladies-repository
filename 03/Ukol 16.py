operace = input('Zadej +, -, * nebo / a ja to spocitam:')
listOfOperations = ['+', '-', '*', '/']
if operace not in listOfOperations:
    print('Neznam tuto operaci, zkus to znovu.')
else:
    prvni_cislo = int(input('Zadej prvni cislo:'))
    druhe_cislo = int(input('Zadej druhe cislo:'))
    vysledek = None

    if operace == '+':
        vysledek = prvni_cislo + druhe_cislo
    elif operace == '-':
        vysledek = prvni_cislo - druhe_cislo
    elif operace == '*':
        vysledek = prvni_cislo * druhe_cislo
    elif operace == '/':
        if druhe_cislo == 0:
            print('Nelze delit nulou')
        else:
            vysledek = prvni_cislo / druhe_cislo

    print(vysledek)

    print('Dekujeme za pouziti kalkulacky')
