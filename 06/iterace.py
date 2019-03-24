print('Slyšela jsem tuto básničku:')
print()

with open('basnicka.txt', encoding='utf-8') as soubor:
    for x in soubor:
        x = x.rstrip()
        print('    ' + x)

print()
print('Jak se ti líbí?')
