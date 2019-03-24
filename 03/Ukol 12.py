from turtle import shape, left, forward, exitonclick, speed

shape('turtle')
speed(100)
# nakresli 50ti uhelnik, co vypada jako spirala

for i in range(300): 
    forward((1 + (i))/50)  # nez se zelva otoci o 360 stupnu, vytvori 50 uhlu
    left(180 - (180 * (1-2/(50))))  # Vnitřní úhel pravidelného n-úhelníka má 180 × (1 - 2/n) stupňů.

exitonclick()
