from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0        
        self.hideturtle()
        self.penup()
        self.goto(0, 330)

    def score_text(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=('Courier', 14, 'bold'))
        
    def game_is_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write("Game Over", move=False, align="center", font=('Courier', 14, 'bold'))

    def increase_score(self):
        self.score += 1

