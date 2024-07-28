from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_velocity = 1
        self.y_velocity = 1
        self.ball_velocity = 0.005
        
    def move(self):
        self.new_x = self.xcor() + self.x_velocity
        self.new_y = self.ycor() + self.y_velocity
        self.goto(self.new_x, self.new_y)

    def bounce_y(self):
        if self.new_y > 290 or self.new_y < -290:
            self.y_velocity *= -1

    def bounce_x(self):
        # if self.new_x > 330 or self.new_x < -330:
        self.x_velocity *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.ball_velocity = 0.005
        self.bounce_x()

    def increase_ball_velocity(self):
        self.ball_velocity *= 0.8
