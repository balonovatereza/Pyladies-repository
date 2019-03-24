from turtle import forward, shape, left, right, exitonclick

# vypise 5 cisel
for cislo in range(5):
    print(cislo)

# vypise pozdravy
for pozdrav in 'Ahoj', 'Hello', 'Hola', 'Hei', 'SYN':
    print(pozdrav + '!')

shape('turtle')
# nakresli kvetinu ze ctvercu
for i in range(18):
    for i in range(4):
        forward(50)
        left(90)
    left(20)

exitonclick()
