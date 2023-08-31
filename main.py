# import libraries
import turtle
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


# import csv
state_df = pd.read_csv("50_states.csv")
states = state_df["state"].tolist()

# loop

while True:

    t1 = Turtle()
    t1.penup()

    user_input = screen.textinput(title="Total 50", prompt="Please guess the state: ")

    if user_input in states:

        result = state_df[state_df["state"] == user_input]
        x_cord = result['x'].tolist()[0]
        y_cord = result['y'].tolist()[0]

        t1.setposition(x=x_cord, y=y_cord)
        t1.write(user_input)


    else:

        print("no match")





turtle.mainloop()
