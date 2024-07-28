from turtle import Turtle
from random import randint
INITIAL_POSITION = 380

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.random_y = randint(-280, 280)
        self.create_random_car()

    def create_random_car(self):
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.goto(INITIAL_POSITION, self.random_y)