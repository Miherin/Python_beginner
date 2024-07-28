from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
# from center_division import CenterDivision

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

# Calls the sides paddle.
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
score.update_score()
# center_division = CenterDivision()

# Moves the sides paddle.
screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_is_on = Trues
while game_is_on:
    time.sleep(ball.ball_velocity)
    screen.update()
    ball.move()
    ball.bounce_y()
    
    if ball.distance(right_paddle) < 63 and ball.xcor() == 330: 
        # ball.setx(320)
        ball.bounce_x()
        ball.increase_ball_velocity()

    if ball.distance(left_paddle) < 63 and ball.xcor() == -330:
        # ball.setx(-330)
        ball.bounce_x()
        ball.increase_ball_velocity()

    if ball.xcor() > 360:
        ball.reset_position()
        score.left_scores()

    if ball.xcor() < -360:
        ball.reset_position()
        score.right_scores()



screen.exitonclick()