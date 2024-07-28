from turtle import Screen
from animal import Animal
from car_option_2 import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)

animal = Animal()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(animal.up, "Up")
screen.onkey(animal.down, "Down")

is_game_on = True
while is_game_on:    
    time.sleep(0.1)
    screen.update()
    car.create_random_car()
    car.move_car()

    if animal.distance(car) < 25:
        is_game_on = False



screen.exitonclick()