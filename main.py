from turtle import Screen
from paddle import Paddle
from ball import Ball
from constant import *
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")
# screen.tracer(0)

r_paddle = Paddle(xcor=(SCREEN_WIDTH / 2) - PADDLE_DISTANCE_FROM_EDGE)
l_paddle = Paddle(xcor=(-SCREEN_WIDTH / 2) + PADDLE_DISTANCE_FROM_EDGE)

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
