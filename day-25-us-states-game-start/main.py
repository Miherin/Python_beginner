import turtle
import pandas as pd

states_path = "50_states.csv"
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv(states_path)
answered_list = []
while True:    
    answer_state = screen.textinput(title=f"{len(answered_list)}/{len(data["state"])} correct.", 
                                    prompt="Guess a States's name.").strip().title()
    if answer_state == '':
        break
    for i in data.state:
        if i == answer_state:
            answered_list.append(i)
            row = data[data.state == answer_state] # Get data of the row of the state guessed.
            # x = row.x.values[0] # Commented out.
            # y = row.y.values[0] # Commented out.
            write_state = turtle.Turtle()
            write_state.hideturtle()
            write_state.penup()
            write_state.goto(row.x.values[0], row.y.values[0]) # Same as the commented out.
            write_state.write(arg=f"{answer_state}")
            
all_states_list = data.state.to_list()
set1 = set(all_states_list)
set2 = set(answered_list)
missing_values = list(set1 - set2)

df = pd.DataFrame(missing_values, columns=['state'])
df.to_csv("states_to_learn.csv")