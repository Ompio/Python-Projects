import turtle

t = turtle.Turtle()
t.speed("fastest")

def kwadrat(dlugosc_boku: int):
    for i in range(4):
        t.forward(dlugosc_boku)
        t.left(90)
