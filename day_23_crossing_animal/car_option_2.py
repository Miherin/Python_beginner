from turtle import Turtle#, Screen
from random import randint
from colors import color_list
import time
INITIAL_POSITION = 350
SPEED = 5

class Car:
    def __init__(self):
        self.cars = []
        self.create_random_car()

    def create_random_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            self.random_y = randint(-250, 250)
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(color_list[randint(0, 5)])
            new_car.penup()
            new_car.goto(INITIAL_POSITION, self.random_y)
            self.cars.append(new_car)

    def move_car(self):        
        for car in self.cars:
            car.backward(SPEED)
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)

