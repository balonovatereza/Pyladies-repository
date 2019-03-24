
soubor_odkud = input('Zadej jmeno souboru, ktery chces kopirovat: ')
soubor_kam = input('Zadej nazev souboru, do ktereho chces zkopirovat obsah'
                   ' puvodniho souboru: ')
try:
    with open(soubor_odkud, encoding='utf-8') as puvodni_soubor:
        precteny_obsah = puvodni_soubor.read()
    with open(soubor_kam, mode='w', encoding='utf-8') as novy_soubor:
        novy_soubor.write(precteny_obsah)
except FileNotFoundError:
    print('Neexistujici soubor, zadej nazev existujiciho souboru.')
else:

    print('Puvodni soubor byl zkopirovan do noveho.')
