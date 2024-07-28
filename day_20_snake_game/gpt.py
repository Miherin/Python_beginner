from turtle import Turtle, Screen

class Snake:
    def __init__(self):
        self.screen = Screen()
        self.snake_segments = []
        self.snake_initial_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        
        self.screen.listen()
        if self.snake_segments[0].heading() != 270:
            self.screen.onkey(lambda: self.snake_segments[0].setheading(90), "w")
        self.screen.onkey(lambda: self.snake_segments[0].setheading(270), "s")
        self.screen.onkey(lambda: self.snake_segments[0].setheading(0), "d")
        self.screen.onkey(lambda: self.snake_segments[0].setheading(180), "a")
    
    def create_snake(self):
        for position in self.snake_initial_positions:
            snake_segment = Turtle(shape="square")
            # snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.snake_segments.append(snake_segment)
    
    def move(self):
        for seg_index in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_index - 1].xcor()
            new_y = self.snake_segments[seg_index - 1].ycor()
            self.snake_segments[seg_index].goto(new_x, new_y)
        
        self.snake_segments[0].forward(20)

# Main game loop
screen = Screen()
snake_game = Snake()

while True:
    snake_game.move()
    screen.update()
