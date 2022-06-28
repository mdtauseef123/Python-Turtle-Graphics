from turtle import Turtle, Screen
my = Turtle()
ss = Screen()


def move_forward():
    my.forward(10)


def move_backward():
    my.backward(10)


def move_left():
    my.left(10)


def move_right():
    my.right(10)


def clear_screen():
    my.clear()
    my.penup()
    my.home()
    my.pendown()


ss.listen()
ss.onkey(key="w", fun=move_forward)
ss.onkey(key="s", fun=move_backward)
ss.onkey(key="a", fun=move_left)
ss.onkey(key="d", fun=move_right)
ss.onkey(key="c", fun=clear_screen)
ss.exitonclick()
