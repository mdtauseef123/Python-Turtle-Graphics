from turtle import Turtle, Screen

my = Turtle()
my.shape("turtle")
my.color("forest green")
for _ in range(10):
    my.forward(10)
    my.penup()
    my.forward(10)
    my.down()


ss = Screen()
ss.exitonclick()

