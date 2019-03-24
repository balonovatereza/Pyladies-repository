from math import pi


def obsah_elipsy(a, b):
    "Vrati obsah elipsy danych rozmeru."
    return pi * a * b


print('Obsah elipsy s osami 4 a 6 cm je', obsah_elipsy(4, 6), 'cm2.')


obsah = 0
a = 30


def obsah_elipsy(a, b):
    obsah = pi * a * b  # Přiřazení do `obsah`
    a = a + 3  # Přiřazení do `a`
    return obsah


print(obsah_elipsy(a, 20))
print(obsah)
print(a)

print('--\N{LATIN SMALL LETTER L WITH STROKE}--')
print('--\N{SECTION SIGN}--')
print('--\N{PER MILLE SIGN}--')
print('--\N{BLACK STAR}--')
print('--\N{SNOWMAN}--')
print('--\N{KATAKANA LETTER TU}--')
retezec = 'Ahoj'
print(retezec.upper())
print(retezec.lower())
print(retezec)


jmeno = input('Zadej jmeno: ')
prijmeni = input('Zadej prijmeni: ')
inicialy = jmeno[0] + prijmeni[0]
print('Tvoje inicialy jsou: ', inicialy.upper())
