def pocet_jednotlivych_znaku2(text):
    pocty_pismen = {}
    for pismeno in range(len(text)):
        pocty_pismen[text[pismeno]] = text.count(text[pismeno])
    return pocty_pismen


text = 'Tempora mutantur et nos mutamur in illis.'


def vypis_slovnik(slovnik):
    for klic, hodnota in slovnik.items():
        print('Klic {}: hodnota {}'.format(klic, hodnota))


vypis_slovnik(pocet_jednotlivych_znaku2(text))
