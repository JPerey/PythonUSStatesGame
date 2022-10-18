from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.goto(100, 100)
        self.FONT = ("Courier", 10, "normal")
        self.hideturtle()
        self.score = 0

    def print_score(self):
        self.clear()
        self.goto(330, 220)
        self.write(f"{self.score}/50", True, align="center", font=self.FONT)

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score
