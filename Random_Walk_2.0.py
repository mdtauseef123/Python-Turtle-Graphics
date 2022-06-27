import turtle
import random
my = turtle.Turtle()
my.pensize(15)
my.speed(0)
turtle.colormode(255)
moves = ["left", "right"]


def move_turtle(direction):
    if direction == "left":
        my.forward(50)
        my.left(90)
    else:
        my.forward(50)
        my.right(90)


def random_colors():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	t = (r, g, b)
	return t


colors = ["forest green", "aquamarine", "dark red", "gold", "dark magenta", "tomato", "pale goldenrod", "moccasin"]
for _ in range(100):
    my.color(random_colors())
    move = random.choice(moves)
    move_turtle(move)

ss = turtle.Screen()
ss.exitonclick()
