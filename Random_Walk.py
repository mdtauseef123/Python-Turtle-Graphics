from turtle import Turtle, Screen
import random
my = Turtle()
my.pensize(10)#For increasing the width of pen
my.speed(0)#For increasing the speed of turtle
moves = ["left", "right"]


def move_turtle(dir):
    if dir == "left":
        my.forward(50)
        my.left(90)
    else:
        my.forward(50)
        my.right(90)


colors = ["forest green", "aquamarine", "dark red", "gold", "dark magenta", "tomato", "pale goldenrod", "moccasin"]
for _ in range(100):
    my.color(random.choice(colors))
    move = random.choice(moves)
    move_turtle(move)

ss = Screen()
ss.exitonclick()
