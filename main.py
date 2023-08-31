# import libraries
import pandas as pd
from turtle import Turtle, Screen

# initialize variables from Turtle() & Screen() class
map = Turtle()
screen = Screen()

# set properties for the canvas
image = "blank_states_img.gif"
screen.addshape(image)
map.shape(image)
map.penup()
screen.title("Guess the US 50 States")


# import csv
state_df = pd.read_csv("50_states.csv")
states = state_df["state"].tolist()

# loop

right_answer = 0
num_of_states = len(states)
guessed_states = []

while right_answer <= num_of_states:

    # creates a new instance of turtle on every guess and sets properties

    t1 = Turtle()
    t1.penup()
    t1.hideturtle()

    # prompt string
    title = f"{right_answer} out of {num_of_states}"

    # collects user's inputs
    user_input = screen.textinput(title=title, prompt="Please guess the state: ")

    # checks if the user guessed the state right and if yes then places the mark on the map

    if user_input in states and user_input not in guessed_states:

        result = state_df[state_df["state"] == user_input]
        x_cord = result['x'].tolist()[0]
        y_cord = result['y'].tolist()[0]

        t1.setposition(x=x_cord, y=y_cord)
        t1.write(user_input)

        right_answer = right_answer + 1
        guessed_states.append(user_input)

    else:
        print("no match")


turtle.mainloop()
