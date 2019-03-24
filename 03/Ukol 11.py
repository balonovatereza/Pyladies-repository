from turtle import shape, left, forward, exitonclick

shape('turtle')

# nakresli 8uhelnikovy ornament a zastavi se po provedeni 40ti uhlu

for i in range(40):
    forward(5 + (i))
    left(180 - (180 * (1-2/(8))))  # Vnitřní úhel pravidelného n-úhelníka má 180 × (1 - 2/n) stupňů.

exitonclick()
