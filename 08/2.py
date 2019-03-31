def pocet_jednotlivych_znaku1(text):
    seznam_dvojic = []
    seznam = list(text)
    for pismeno in seznam:
        if pismeno not in seznam_dvojic:
            dvojice = pismeno, seznam.count(pismeno)
            seznam_dvojic.append(dvojice)
    seznam_dvojic.sort()
    pocty_pismen = dict(seznam_dvojic)
    return pocty_pismen


print(pocet_jednotlivych_znaku1('Tempora mutantur et nos mutamur in illis.'))


def pocet_jednotlivych_znaku2(text):
    pocty_pismen = {}
    for pismeno in range(len(text)):
        pocty_pismen[text[pismeno]] = text.count(text[pismeno])
    return pocty_pismen


print(pocet_jednotlivych_znaku2('Tempora mutantur et nos mutamur in illis.'))


def pocet_jednotlivych_znaku3(text):
    '''

    '''
    pocty_pismen = {}
    for i in range(len(text)):
        pocty_pismen.setdefault(text[i], text.count(text[i]))
    return pocty_pismen


print(pocet_jednotlivych_znaku3('Tempora mutantur et nos mutamur in illis.'))
