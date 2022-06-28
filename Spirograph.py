import turtle
import random
my = turtle.Turtle()
turtle.colormode(255)
my.speed(0)


def generate_colors():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	t = (r, g, b)
	return t


def draw_spirograph(size_of_gap):
	for _ in range(int(360/size_of_gap)):
		my.color(generate_colors())
		my.circle(100)
		my.setheading(my.heading()+size_of_gap)


draw_spirograph(5)

ss = turtle.Screen()
ss.exitonclick()
