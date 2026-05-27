from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.pu()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

        # setting ball direction
        direction = ("left", "right")
        angle = random.randint(-45, 45)
        curr_head = self.heading()
        if random.choice(direction) == "left":
            angle = 180 - angle
            self.setheading(curr_head + angle)
        else:
            self.setheading(curr_head + angle)

    def move(self):
        x_new  = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new,y_new)


    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
