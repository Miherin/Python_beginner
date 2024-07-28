from turtle import Turtle
MOVE_DISTANCE = 20
INITIAL_POSITION = (0, -280)

class Animal(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('blue')
        self.setheading(90)
        self.goto(INITIAL_POSITION)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        # self.check_position()

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
        # self.check_position()

    def reset_position(self):
        self.goto(0, -280)

    # def check_position(self):
    #     if self.ycor() >= 280:
    #         print('crossed')
