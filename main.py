import pandas as pd
from turtle import Turtle, Screen

# Setting up screen
screen = Screen()
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")

# Read data
data = pd.read_csv("50_states.csv")
state_set = set(data['state'])

# Create turtle
labeler = Turtle()
labeler.hideturtle()
labeler.penup()

labeled_states = set()
score = 0

while True:
    inp = screen.textinput(f'{int(score)}/50', "Enter a state name:")  # Prompt for user input
    inp = inp.title()  # Convert the input to title case

    if inp in state_set and inp not in labeled_states:  # Check if input is a valid state and not labeled already
        state_data = data[data["state"] == inp]  # Get the data for the state
        x = int(state_data['x'].iloc[0])  # Get the x-coordinate
        y = int(state_data['y'].iloc[0])  # Get the y-coordinate

        labeler.goto(x, y)  # Move the turtle to the state's coordinates
        labeler.write(state_data['state'].item())  # Write the state name on the screen
        labeled_states.add(inp)  # Add the labeled state to the set
        score += 1  # Increment the score

    if len(labeled_states) == 50:  # Check if all states have been labeled
        break

screen.mainloop()  # Start the event loop
