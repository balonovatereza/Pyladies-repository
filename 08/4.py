import random

# Úkolem je vytvořit známou skautskou hru „Kdo? S kým? Co dělali?“. Hra se
# hráče zeptá postupně na různé otázky, například „Kdo?“, „S kým?“,
# „Co dělali?“, „Kde?“, „Kdy?“, a nakonec „Proč?“, s tím, že mu umožní na
# jednu otázku odpovědět vícekrát a všechny odpovědi si uloží. Na závěr pak
# hra z každé sady odpovědí vybere náhodně jednu odpověď a z takto vybraných
# odpovědí složí větu, kterou vypíše uživateli. Seznam otázek by mělo být možné
# změnit v kódu na jednom místě bez zásahu do logiky programu.


seznam_otazek = ['Kdo', 'Kde', 'Kdy', 'S kym', 'Co delali', 'Proc']
slovnik_odpovedi = {}

for otazka in seznam_otazek:
    slovnik_odpovedi[otazka] = []

for otazka in seznam_otazek:
    print('Pro prechod k dalsi otazce zadej \'x\'')
    while True:
        odpoved = input('{}:\n'.format(otazka))
        odpoved_ = odpoved.strip().lower()
        if odpoved_ == 'x':
            if len(slovnik_odpovedi[otazka]) == 0:
                slovnik_odpovedi[otazka].append('nezadano')
            break
        else:
            slovnik_odpovedi[otazka].append(odpoved_)

for otazka in seznam_otazek:
    seznam_odpovedi = slovnik_odpovedi[otazka]
    nahodne_cislo = random.randint(0, len(seznam_odpovedi) - 1)
    print(seznam_odpovedi[nahodne_cislo], end=' ')
