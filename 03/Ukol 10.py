from turtle import shape, left, forward, exitonclick

shape('turtle')

# nakresli hranaty ornament

for i in range(19):  # zelva se skonci otacet o 90 stupnu po tom co vytvori 19 uhlu
    left(90)
    forward(5 + 3 * i)

exitonclick()
