from colors import extracted_color_list
import random
import turtle as t

'''import colorgram
### How to extract colors from images using colorgram. ###
rgb_list = []
color_pallet = colorgram.extract('hirst.jpg', 50)

for color in color_pallet:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_list.append(new_color)
print(rgb_list)'''

mike = t.Turtle()
mike.hideturtle()
t.colormode(255)
mike.pu()
mike.speed("fastest")
up = -250

def draw_dots(lenght):
    mike.teleport(-350, lenght)
    for _ in range(15):
        random_color = random.choice(extracted_color_list)
        mike.dot(20, random_color)
        mike.forward(50)
        
for _ in range(11):
    draw_dots(up)
    up += 50


screen = t.Screen()
screen.exitonclick()

