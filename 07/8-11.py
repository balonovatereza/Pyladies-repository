with open('basnicka.txt', encoding='utf-8') as soubor:
    kytice = soubor.read()


def obrat_poradi_versu(text):
    seznam = text.split('\n')
    seznam.reverse()

    for radek in seznam:
        print(radek)


obrat_poradi_versu(kytice)


def obrat_poradi_slov(text):
    seznam = text.split('\n')

    for radek in seznam:
        slova = radek.split(' ')
        slova.reverse()
        print(' '.join(slova))


obrat_poradi_slov(kytice)


def obrat_poradi_slok(text):
    seznam = text.split('\n\n')
    seznam.reverse()

    for sloka in seznam:
        print(sloka, end='\n\n')


obrat_poradi_slok(kytice)
