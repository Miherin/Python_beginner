# Turtle is an existent class in-built in Python.
from turtle import Turtle, Screen

# when assigning a class to a variable, it now becomes an object.
mike = Turtle()
print(mike)

# shape, color, movement and much more are in-built commands.
mike.shape("turtle")
mike.color("green", "aquamarine")
mike.forward(100)

# a little loop for fun to explore the possibilities.
while True:
    mike.forward(200)
    mike.left(170)
    if abs(mike.pos()) < 1:
        break

# in-built screen command.
my_screen = Screen()
print(my_screen.canvwidth)
my_screen.exitonclick()