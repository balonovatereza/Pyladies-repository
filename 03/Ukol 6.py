from turtle import shape, left, forward, exitonclick, penup, pendown

shape('turtle')

for i in range(4):  #
    for j in range(5 + i):  # nakresli 5ti uhelnik a pak postupne kresli obrazce s poctem uhlu o jeden vetsi, dokud jich nenakresli i kusu
        forward(200/(5 + i))
        left(180 - (180 * (1-2/(5 + i))))  # Vnitřní úhel pravidelného n-úhelníka má 180 × (1 - 2/n) stupňů.

    penup()
    forward(100)
    pendown()

exitonclick()
