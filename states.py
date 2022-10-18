import pandas


class States:

    def __init__(self):
        self.states_data = pandas.read_csv("50_states.csv")
        self.states_list = self.states_data["state"].to_list()
        self.current_state = []

    def check_answer(self, player_answer):
        for state in self.states_list:
            if player_answer == state.lower():
                print("correct!")
                return state
        return "incorrect"

    def give_coordinates(self, state):
        self.current_state = self.states_data[self.states_data["state"] == state]
        return self.current_state
