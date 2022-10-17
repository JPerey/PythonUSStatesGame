from turtle import Turtle


class TextPlacer(Turtle):

    def __init__(self):
        super().__init__()

    def place_state(self, x, y, state):
        new_state = Turtle()
        new_state.coordinate_x = x
        new_state.coordinate_y = y
        new_state.FONT = ("Courier", 10, "normal")
        new_state.shape("square")
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(new_state.coordinate_x, new_state.coordinate_y)
        new_state.write(f"{state}", True, align="center", font=new_state.FONT)
