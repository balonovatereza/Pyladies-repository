from turtle import shape, left, forward, exitonclick

shape('turtle')

# program vykresli 95uhelnik

pocet_uhlu = 95

for i in range(pocet_uhlu):
    forward(200/(pocet_uhlu))
    left(180 - (180 * (1-2/(pocet_uhlu))))  # Vnitřní úhel pravidelného n-úhelníka má 180 × (1 - 2/n) stupňů.

exitonclick()
