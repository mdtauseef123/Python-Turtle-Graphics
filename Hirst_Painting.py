import turtle
import random
turtle.colormode(255)
my = turtle.Turtle()
my.speed(0)
my.penup()
my.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]
my.setheading(225)
my.forward(300)
my.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    my.dot(20, random.choice(color_list))
    my.forward(50)
    if dot_count % 10 == 0:
        my.setheading(90)
        my.forward(50)
        my.setheading(180)
        my.forward(500)
        my.setheading(0)
ss = turtle.Screen()
ss.exitonclick()
