from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 260)
        self.write(self.l_score, move=False, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 260)
        self.write(self.r_score, move=False, align="center", font=("Courier", 80, "normal"))

    def left_miss(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def right_miss(self):
        self.l_score +=1
        self.clear()
        self.update_scoreboard()