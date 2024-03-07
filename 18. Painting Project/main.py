import random
from turtle import Turtle, Screen, colormode

turt = Turtle()
turt.speed("fastest")
colormode(255)
turt.up()
turt.setpos(-350, 350)
turt.down()

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def drawCircle():
    for i in range(1, 101):
        turt.color(randomColor())
        turt.begin_fill()
        turt.circle(20)
        turt.end_fill()
        if i % 10 == 0:
            turt.up()
            turt.setx(-350)
            turt.sety(turt.ycor() - 50)
            turt.down()

        else:
            turt.up()
            turt.forward(50)
            turt.down()


drawCircle()
screen = Screen()
screen.exitonclick()