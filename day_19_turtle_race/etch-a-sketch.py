from turtle import Turtle, Screen

nick = Turtle()
screen = Screen()
nick.speed(0)


def forwards():
    nick.forward(20)

def backwards():
    nick.backward(20)

def move_left(): # She complicates an easy command
    left_heading = nick.heading() + 10
    nick.setheading(left_heading)
    # nick.left(10)

def move_right():
    nick.right(10)

def clear_screen():
    nick.clear()

screen.listen()

screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")

screen.onkey(clear_screen, "space")

# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="w", fun=move_up)
# screen.onkey(key="s", fun=move_down)

screen.exitonclick()
