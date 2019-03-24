with open('basnicka.txt', encoding='utf-8') as soubor:
    kytice = soubor.read()


def obrat_poradi_versu(text):
    seznam = text.split('\n')
    seznam.reverse()

    for radek in seznam:
        print(radek)


obrat_poradi_versu(kytice)
