with open('katakana.txt', encoding='utf-8') as soubor:
    obsah_katakany = soubor.read()
    with open('rozsypanycaj.txt', encoding='utf-8') as soubor:
        obsah_stranky = soubor.read()
        pocitadlo = 0
        for znak in obsah_katakany:
            if znak == '\n':
                continue
            pocet_znaku = obsah_stranky.count(znak)
            pocitadlo = pocitadlo + pocet_znaku
        print('Pocet znaku katakany: ', pocitadlo)

with open('hiragana.txt', encoding='utf-8') as soubor:
    obsah_hiragany = soubor.read()
    with open('rozsypanycaj.txt', encoding='utf-8') as soubor:
        obsah_stranky = soubor.read()
        pocitadlo = 0
        for znak in obsah_hiragany:
            if znak == '\n':
                continue
            pocet_znaku = obsah_stranky.count(znak)
            pocitadlo = pocitadlo + pocet_znaku
        print('Pocet znaku hiragany: ', pocitadlo)

with open('katakana.txt', encoding='utf-8') as soubor:
    katakana = soubor.read()
with open('hiragana.txt', encoding='utf-8') as soubor:
    hiragana = soubor.read()
with open('rozsypanycaj.txt', encoding='utf-8') as soubor:
    rozsypanycaj = soubor.read()


def pocitani_znaku(abeceda, text):
    pocitadlo = 0
    for delka_textu in range(len(text)):
        for delka_abecedy in range(len(abeceda)):
            if abeceda[delka_abecedy] in text[delka_textu]:
                if abeceda[delka_abecedy] == ' ' or abeceda[delka_abecedy] == '\n':
                    continue
                else:
                    pocitadlo += 1
    return pocitadlo


print('Znaku hiragany je: ', pocitani_znaku(obsah_hiragany, rozsypanycaj))
print('Znaku hiragany je: ', pocitani_znaku(obsah_katakany, rozsypanycaj))
