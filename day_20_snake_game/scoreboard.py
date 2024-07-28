from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.clear()
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.write(f"Score: {self.score}", move=False, align="center", font=('Courier', 14, 'bold'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center", font=('Courier', 14, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=('Courier', 16, 'bold'))
