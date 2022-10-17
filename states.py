import pandas


class States:

    def __init__(self):
        self.states_data = pandas.read_csv("50_states.csv")
        self.states_list = self.states_data["state"].to_list()

    def check_answer(self, player_answer):
        for state in self.states_list:
            if player_answer == state.lower():
                print("correct!")
                return state
        return "incorrect"
