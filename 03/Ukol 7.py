from turtle import shape, left, forward, exitonclick

shape('turtle')
pocet_uhlu = int(input('Zadej pocet uhlu n-uhelniku:'))

for i in range(pocet_uhlu):  # vykresli obrazec s poctem uhlu jaky zada uzivatel
    forward(200/(pocet_uhlu))
    left(180 - (180 * (1-2/(pocet_uhlu))))  # Vnitřní úhel pravidelného n-úhelníka má 180 × (1 - 2/n) stupňů.

exitonclick()
