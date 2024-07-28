import turtle as t
from color_list import color_list
import random

mike = t.Turtle()
mike.shape("turtle")
t.colormode(255)
mike.color("teal")
# mike.teleport(-385)

## Task 1 - Drawing dashed line
# for _ in range(38):
#     mike.pu()    
#     mike.forward(10)
#     mike.pd()
#     mike.forward(10)

## Task 2 - Drawing different iridescent shapes
# def draw_shape(sides, lenght):
#     angle = 360 / sides
#     for _ in range(sides):
#         mike.right(angle)
#         mike.forward(lenght)

# for sides in range(4, 11):
#     mike.color(random.choice(color_list))
#     draw_shape(sides, 40)

## Task 3 - Random Walk
# mike.width(5)
# mike.speed("fastest")
# def turn_right():
#     mike.right(90)

# def turn_left():
#     mike.left(90)

# def forwards():
#     mike.forward(15)

# direction_list = [turn_right, turn_left, forwards]

# for _ in range(100):
#     mike.color(random.choice(color_list))
#     mike.forward(10)
#     random.choice(direction_list)()

## Tuples and random RGB colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# direction_list = [0, 90, 180, 270]

# for _ in range(100):
#     mike.color(random_color())
#     mike.forward(10)
#     mike.setheading(random.choice(direction_list))

## Drawing a Spirograph

mike.speed("fastest")

for direction in range(1, 361, 5):
    mike.color(random_color())
    mike.circle(100)
    mike.setheading(direction)






screen = t.Screen()
screen.exitonclick()