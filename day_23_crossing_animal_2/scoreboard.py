from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1    
        self.penup()
        self.score_text()

    def score_text(self):
        self.hideturtle()
        self.goto(-280, 280)
        self.write(f"Level {self.level}", move=False, align="center", font=('Courier', 18, 'bold'))
        
    def game_is_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.write("Game Over", move=False, align="center", font=('Courier', 14, 'bold'))

    def increase_score(self):
        self.clear()
        self.level += 1
        self.score_text()

