import random

with open('basnicka.txt', encoding='utf-8') as soubor:
    kytice = soubor.read()


def vypis_slova_nahodne(text):
    '''
    Vypise slova basne v nahodnem poradi.
    '''
    seznam = text.split(' ')
    print(seznam)
    random.shuffle(seznam)
    print(seznam)


print(vypis_slova_nahodne(kytice))
