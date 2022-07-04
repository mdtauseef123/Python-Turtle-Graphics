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
    #To clear the screen
    my.clear()
    #When we are moving back to the origin position it shouldn't mark the way
    my.penup()
    #To move back to the original position i.e. origin(0,0)
    my.home()
    #As we reach to the origin position now we will pen up so that we can do the function again
    my.pendown()


ss.listen()
ss.onkey(key="w", fun=move_forward)
ss.onkey(key="s", fun=move_backward)
ss.onkey(key="a", fun=move_left)
ss.onkey(key="d", fun=move_right)
ss.onkey(key="c", fun=clear_screen)
ss.exitonclick()
