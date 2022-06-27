from turtle import Turtle, Screen

my = Turtle()


def make_shapes(sides, req_angle):
    for _ in range(sides):
        my.right(req_angle)
        my.forward(100)


side = 3
colors = ["forest green", "aquamarine", "dark red", "gold", "dark magenta", "tomato", "pale goldenrod", "moccasin"]
my.forward(100)
for i in range(8):
    my.color(colors[i])
    make_shapes(side, 360/side)
    side += 1


ss = Screen()
ss.exitonclick()
