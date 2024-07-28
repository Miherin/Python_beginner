from turtle import Turtle, Screen
import turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -120
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.teleport(x=-230, y=y_position)
    new_turtle.color(colors[turtle_index])
    y_position += 50
    all_turtles.append(new_turtle)

while True:
    user_bet = turtle.textinput(title="Vote for the winner!",prompt="Which color do you think will win the race?: ")
    if user_bet in colors:
        is_race_on = True
        break
    else:
        turtle.reset()
        turtle.hideturtle()
    
while is_race_on:
    for turtle_x in all_turtles:
        if turtle_x.xcor() > 230:            
            if turtle_x.pencolor() == user_bet:
                print(f"{turtle_x.pencolor()} you won!")
                is_race_on = False
            else:
                print(f"{turtle_x.pencolor()} won! Game over!")
                is_race_on = False
    
        turtle_x.penup()
        random_number = random.randint(0, 10)
        turtle_x.fd(random_number)
    








screen.exitonclick()
