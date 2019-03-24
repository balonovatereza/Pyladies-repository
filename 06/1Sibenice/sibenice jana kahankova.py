from random import choice

def vypis(pokus):
    """
    Načítá obrázky ze souboru podle čísla pokusu.
    """
    while True:
        #nazev = str(pokus) + '.txt'
        soubor = open(str(pokus) + '.txt', encoding = 'utf-8')
        obrazek = soubor.read()
        soubor.close()
        print(obrazek)
        break

def dopln(hadanka, pozice, znak):
    """
    Doplní do řetězce zadané písmeno.
    """
    return hadanka[:pozice] + znak + hadanka[pozice + 1:]

def tahHrace():
    """
    Ptá se hráčky na písmeno, které by chtěla doplnit. Následně vyhodnocuje, zda
    je toto písmeno v hádaném slově, či nikoli.
    """
    while True:
        znak = input('Zadej písmeno:')
        if len(znak) == 1:
            znak = znak.lower() #ošetření pro velká písmena
            return znak
        else:
            print('Zadala jsi číslo nebo řetězec.')

def hraSibenice():
    """
    Hra šibenice.
    """
    slovo = choice(("hora", "slunce", "mrak"))
    #print(slovo)
    hadanka = len(slovo) * '-'
    print(hadanka)
    pokus = 0
    while hadanka != slovo:
        znak = tahHrace()
        if znak in slovo:
            pozice = slovo.index(znak)
            hadanka = dopln(hadanka, pozice, znak)
            print(hadanka)
        else:
            pokus += 1
            vypis(pokus)
            print('Písmeno', znak, 'se v hledaném slově nevyskytuje.')
            print(hadanka)
            if pokus == 10:
                print('A visíš! Došly ti pokusy. Hledaným slovem bylo slovo', slovo)
                break
    else:
        print('Vyhrála jsi! Hádané slovo je:', hadanka)

hraSibenice()
