from turtle import Turtle, Screen
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.random_y = random.randint(-250, 250)
        self.create_random_car()

    def create_random_car(self):
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.setheading(180)
        self.goto(300, self.random_y)

class MovingObject(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.goto(0, 0)
        self.direction = 'up'
    
    def move(self):
        global car_speed  # Use the global car_speed variable
        if self.direction == 'up':
            self.sety(self.ycor() + 20)
            if self.ycor() >= 290:
                self.goto(0, 0)  # Reset to starting position
                self.direction = 'up'
                car_speed += 1  # Increase car speed
        else:
            self.sety(self.ycor() - 20)
            if self.ycor() <= -250:
                self.direction = 'up'

def create_new_car():
    new_car = Car()
    cars.append(new_car)
    screen.ontimer(create_new_car, random.randint(1000, 3000))  # Create new car every 1-3 seconds

def move_cars():
    global car_speed  # Use the global car_speed variable
    for car in cars:
        car.forward(car_speed)
        if car.xcor() < -300:
            car.hideturtle()
            cars.remove(car)
    screen.update()  # Manually update the screen to show car movements
    screen.ontimer(move_cars, 20)  # Move cars every 20 milliseconds

def check_collisions():
    for car in cars:
        if moving_object.distance(car) < 20:  # Collision detection
            print("Collision detected!")
            screen.bye()  # Close the window and end the screen loop
            return
    screen.ontimer(check_collisions, 100)  # Check for collisions every 100 milliseconds

def move_object():
    moving_object.move()
    screen.update()  # Manually update the screen to show object movements
    screen.ontimer(move_object, 100)  # Move object every 100 milliseconds

cars = []
car_speed = 2  # Initialize car speed
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Disable automatic screen updates

moving_object = MovingObject()

create_new_car()  # Start creating cars
move_cars()       # Start moving cars
check_collisions()  # Start checking for collisions
move_object()       # Start moving the object

screen.mainloop()
