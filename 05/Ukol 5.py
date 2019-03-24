def ano_nebo_ne(otazka):
    "Vrátí True nebo False, podle odpovědi uživatele"
    while True:
        odpoved = input(otazka)
        if odpoved.strip().lower() == ('ano' or 'a'):
            return True
        elif odpoved.strip().lower() == ('ne' or 'n'):
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')


if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')
