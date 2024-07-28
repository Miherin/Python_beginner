from turtle import Screen
from animal import Animal
from car import Car
from colors import color_list
from random import randint
from scoreboard import Scoreboard
import time

# Create screen and define parameters
screen = Screen()
screen.setup(width=800, height=700)
screen.title("Crossing Animal")
screen.tracer(0)

# Global variable
SPEED = 3

def create_new_car():
    if len(car_list) < len(color_list):
        new_car = Car()
        new_car.color(color_list[randint(0, 17)])
        car_list.append(new_car)
        screen.ontimer(create_new_car, randint(200, 1000))

def move_cars():
    global SPEED
    for car in car_list:
        car.forward(SPEED)
        if car.xcor() < -400:  # If the car moves out of the screen
            car.hideturtle()
            car_list.remove(car)
            if animal.ycor() > 280: # If animal reaches the other side
                scoreboard.increase_score()
                screen.update()
                animal.reset_position()
                SPEED += 1
                # SCORE += 1
                time.sleep(2)
    screen.update() # Manually update the screen to show car movements
    screen.ontimer(move_cars, 20) # Move cars every 20 milliseconds

def check_collisions():
    for car in car_list:
        if animal.distance(car) < 25:  # Collision detection
            scoreboard.game_is_over()
            screen.update()
            time.sleep(100)
            # print("Collision detected!")
            # screen.bye()
    screen.ontimer(check_collisions, 100)

animal = Animal()
scoreboard = Scoreboard()
car_list = []

screen.listen()
screen.onkey(animal.up, "w")
screen.onkey(animal.down, "s")
screen.update()

scoreboard.score_text()
create_new_car()
move_cars()
check_collisions()

screen.mainloop()