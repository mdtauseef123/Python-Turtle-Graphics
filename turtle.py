from turtle import Turtle, Screen
ss = Screen()
ss.setup(width=500, height=400)
#choice = ss.textinput(title="Bet the race", prompt="Which turtle will win the race? Enter the color: ")
red = Turtle("turtle")
red.penup()
red.color("red")
orange = Turtle("turtle")
orange.penup()
orange.color("orange")
yellow = Turtle("turtle")
yellow.penup()
yellow.color("yellow")
green = Turtle("turtle")
green.penup()
green.color("green")
blue = Turtle("turtle")
blue.penup()
blue.color("blue")
purple = Turtle("turtle")
purple.penup()
purple.color("purple")
red.goto(x=-230, y=-100)
orange.goto(x=-230, y=-60)
yellow.goto(x=-230, y=-20)
green.goto(x=-230, y=20)
blue.goto(x=-230, y=60)
purple.goto(x=-230, y=100)
ss.exitonclick()