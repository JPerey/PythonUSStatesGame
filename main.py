from turtle import Screen, Turtle
from states import States
import pandas

screen = Screen()
state = States()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.title("US 50 States Game")
screen.tracer(0)
screen.listen()
screen.update()


def player_answer():
    player_state = screen.textinput("Name a state", "Please input a state for consideration: ").lower()
    decision = state.check_answer(player_state)
    print(decision)


# timeline

player_answer()

screen.exitonclick()


# 1: pull data from csv into a class
# 2: create a screen with the image
# 3: create loop that checks for correct answers to US states
# 4: if answer is found, place US state name turtle in correct place via the csv

# functions

def create_screen():
    pass
