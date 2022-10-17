from turtle import Screen
from states import States
from placer import TextPlacer

screen = Screen()
state = States()
placer = TextPlacer()

screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.title("US 50 States Game")
screen.tracer(0)
screen.listen()
screen.update()


def player_answer():
    player_state = screen.textinput("Name a state", "Please input a state for consideration: ").lower()
    decision = state.check_answer(player_state)
    if decision != "incorrect":
        place_answer(decision)
        get_score()


def place_answer(state_to_place):
    state_to_place_info = state.give_coordinates(state_to_place)
    x = state_to_place_info["x"].to_list()
    y = state_to_place_info["y"].to_list()
    placer.place_state(x[0], y[0], state_to_place)
    print(x[0])
    # get coordinates from states.py


def get_score():
    score = state.increase_score()


# timeline

player_answer()

screen.exitonclick()

# 1: pull data from csv into a class X
# 2: create a screen with the image X
# 3: create loop that checks for correct answers to US states
# 4: if answer is found, place US state name turtle in correct place via the csv

# functions
