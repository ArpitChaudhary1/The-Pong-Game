from turtle import Screen
from pads import Pads
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(1300,750)
screen.title("The Pong Game")


screen.tracer(0)
l_pad = Pads((-630,0))
r_pad = Pads((620,0))
ball = Ball()
scoreboard = Scoreboard()

screen.update()


screen.listen()
screen.onkey(l_pad.up,"w")
screen.onkey(l_pad.down,"s")
screen.onkey(r_pad.up,"Up")
screen.onkey(r_pad.down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()


    # collision with the walls
    if ball.ycor() >= 350 or ball.ycor() <= -350:
        ball.bounce_y()

    # collision with the paddle
    if ball.distance(l_pad) < 50 and ball.xcor() <-605  or  ball.distance(r_pad) < 50 and ball.xcor() >595:
        ball.bounce_x()


    # ball miss right paddle
    if ball.xcor() > 630 :
        ball.reset_position()
        scoreboard.right_miss()

    # ball misses left paddle
    if ball.xcor() < -630:
        ball.reset_position()
        scoreboard.left_miss()


screen.exitonclick()