from turtle import Screen
from states import States
from placer import TextPlacer
from scoreboard import Scoreboard

screen = Screen()
state = States()
placer = TextPlacer()
scoreboard = Scoreboard()

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
        scoreboard.increase_score()


def place_answer(state_to_place):
    state_to_place_info = state.give_coordinates(state_to_place)
    x = state_to_place_info["x"].to_list()
    y = state_to_place_info["y"].to_list()
    placer.place_state(x[0], y[0], state_to_place)
    # get coordinates from states.py


# timeline
def run():
    game_over = False
    scoreboard.print_score()

    while not game_over:
        player_answer()
        scoreboard.print_score()
        score = scoreboard.get_score()
        if score == 50:
            game_over = True


run()
screen.exitonclick()

# 1: pull data from csv into a class X
# 2: create a screen with the image X
# 3: create loop that checks for correct answers to US states X
# 4: if answer is found, place US state name turtle in correct place via the csv X
# have a time that goes down from 10 minutes, and at 00:00 the game fails

# functions
