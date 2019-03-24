strana = float(input('Zadej stranu ctverce v centimetrech: '))
kladne_cislo = strana > 0
if kladne_cislo:
    print('Obvod ctverce se stranou ', strana, ' je ', 4 * strana, 'cm')
    print('Obsah ctverce se stranou ', strana, ' je ', strana ** 2, 'cm')
else:
    print('Strana ctverce musi byt kladna.')

print('Dekujeme za pouziti geometricke kalkulacky.')
