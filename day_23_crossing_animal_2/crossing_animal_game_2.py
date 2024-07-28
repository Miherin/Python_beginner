from turtle import Screen
from animal import Animal
from car_option_2 import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)

animal = Animal()
cars = Car()
scoreboard = Scoreboard()
# scoreboard.score_text()

screen.listen()
screen.onkey(animal.up, "Up")
screen.onkey(animal.down, "Down")

is_game_on = True
while is_game_on:    
    time.sleep(0.1)
    screen.update()
    cars.create_random_car()
    cars.move_car()

    for car in cars.cars:
        if car.distance(animal) < 25:
            scoreboard.game_is_over()
            is_game_on = False

    if animal.ycor() > 290:
        animal.reset_position()
        scoreboard.increase_score()
        cars.increase_speed()


screen.exitonclick()