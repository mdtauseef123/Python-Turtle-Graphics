from turtle import Turtle, Screen
import random
ss = Screen()
ss.setup(width=500, height=400)
user_bet = ss.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
pos = -100
all_turtles = []
is_race_continue = False
for i in range(0, len(colors)):
    my = Turtle("turtle")
    my.penup()
    my.color(colors[i])
    my.goto(x=-230, y=pos)
    pos += 40
    all_turtles.append(my)

if user_bet:
    is_race_continue = True
while is_race_continue:
    for turtles in all_turtles:
        if turtles.xcor() == 250:
            is_race_continue = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You\'ve won the race. The {winning_color} is the winner.")
            else:
                print(f"You\'ve lost the race. The {winning_color} is the winner.")
        race_distance = random.randint(0, 10)
        turtles.forward(race_distance)
ss.exitonclick()

