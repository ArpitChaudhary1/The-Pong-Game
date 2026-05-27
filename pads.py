from turtle import Turtle

LEFT_POSITIONS = (-630,0)
RIGHT_POSITIONS= (620,0)
MOVE_DISTANCE = 80



class Pads(Turtle):
    def __init__(self,position):
        super().__init__()
        self.pu()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(position)
        self.speed("fastest")


    def up(self):
        new_cor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor() , new_cor)

    def down(self):
        new_cor = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_cor)

