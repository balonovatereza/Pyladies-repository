pole = '_______'
neuspesny_pokus = 0


def vypis_stav(pole, neuspesny_pokus):
    if neuspesny_pokus:
        if neuspesny_pokus == 1:
            print('''






~~~~~~~''')
        elif neuspesny_pokus == 2:
            print('''+
|
|
|
|
|
~~~~~~~ ''')
        elif neuspesny_pokus == 3:
            print('''+---.
|
|
|
|
|
~~~~~~~''')
        elif neuspesny_pokus == 4:
            print('''+---.
|   |
|
|
|
|
~~~~~~~''')
        elif neuspesny_pokus == 5:
            print('''+---.
|   |
|   O
|
|
|
~~~~~~~''')
        elif neuspesny_pokus == 6:
            print('''+---.
|   |
|   O
|   |
|
|
~~~~~~~''')
        elif neuspesny_pokus == 7:
            print('''+---.
|   |
|   O
| --|
|
|
~~~~~~~''')
        elif neuspesny_pokus == 8:
            print('''+---.
|   |
|   O
| --|--
|
|
~~~~~~~''')
        elif neuspesny_pokus == 9:
            print('''+---.
|   |
|   O
| --|--
|  /
|
~~~~~~~''')
        elif neuspesny_pokus == 10:
            print('''+---.
|   |
|   O
| --|--
|  / \\
|
~~~~~~~''')
    elif '_' in pole:
        print(pole)
    elif '_' not in pole:
        print('Gratuluji! Vyhral jsi.')


vypis_stav(pole, neuspesny_pokus)
