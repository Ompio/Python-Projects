import random
import turtle


t = turtle.Turtle()
t.speed("fast")
turtle.bgcolor("black")
t.pencolor("lime")
t.pensize(2)
# t.penup()
# t.goto(-300, -300)
# t.pendown()

def random_color():
    # Generowanie losowych wartości RGB
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Konwertowanie do formatu heksadecymalnego
    return f'#{r:02x}{g:02x}{b:02x}'


def kwadrat(dlugosc_boku: int):
    for i in range(4):
        t.forward(dlugosc_boku)
        t.left(90)

kwadrat(4)

# kwadrat(4)


def fractal_daktal(rozmiar_najwiekszego_kwadratu: int, krok):
    kwadrat(rozmiar_najwiekszego_kwadratu)
    if rozmiar_najwiekszego_kwadratu > 1:
        fractal_daktal(int(rozmiar_najwiekszego_kwadratu * krok), krok)

t.right(90)
fractal_daktal(500, 0.9)
t.left(90)
def sierpinski(rozmiar, kroki):
    if kroki > 0:
        for i in range(3):
            t.pencolor(random_color())
            t.forward(rozmiar)
            t.left(120)
            sierpinski(rozmiar/2, kroki-1)


class drzewo_z_liscmi():
    def __init__(self, wielkosc_drzewka, kat, redukcja_dlugosci, grubosc):
        self.wielkosc_drzewka = wielkosc_drzewka
        self.redukcja_dlugosci = redukcja_dlugosci
        self.grubosc = grubosc
        self.kat = kat
        self.grubosc_zulwia = 10

    def print(self):
        t.left(90)
        self.lodyzka(100, self.wielkosc_drzewka, self.grubosc)
        t.left(180)

    def lodyzka(self, odleglosc, ilosc_galazek, grubosc):
        if ilosc_galazek > 0:
            t.pensize(grubosc)
            t.forward(odleglosc)
            t.left(self.kat / 2)
            self.lodyzka(odleglosc * self.redukcja_dlugosci, ilosc_galazek-1, grubosc*0.7)
            t.right(self.kat)
            self.lodyzka(odleglosc * self.redukcja_dlugosci, ilosc_galazek-1, grubosc*0.7)
            t.left(self.kat / 2)
            t.backward(odleglosc)
        else:
            self.lisc()

    def lisc(self):
        if random.randint(1, 100) <= 15:
            random_orientation = random.randint(50, 250)
            t.right(random_orientation)
            t.pencolor('red')
            t.fillcolor('orange')
            t.begin_fill()
            t.circle(5)
            t.end_fill()
            t.pencolor("lime")
            t.left(random_orientation)

class niesierpinski():
    def __init__(self, rozmiar, kroki):
        self.rozmiar = rozmiar
        self.kroki = kroki

    def print(self):
        # t.left(90)
        self.kwadrat(self.rozmiar, self.kroki)

    def kwadrat(self, rozmiar, kroki):
        if kroki > 0:
            for i in range(4):
                t.pencolor(random_color())
                t.forward(rozmiar/2)
                self.kwadrat(rozmiar/2, kroki-1)
                t.left(90)


sierpinski(500, 4)

drzewko = drzewo_z_liscmi(5,60,0.8,8)
drzewko.print()
niesierpinski = niesierpinski(500, 4)
t.right(90)
niesierpinski.print()
turtle.exitonclick()