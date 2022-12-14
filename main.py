from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from constant import *
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(xcor=(SCREEN_WIDTH / 2) - PADDLE_DISTANCE_FROM_EDGE)
l_paddle = Paddle(xcor=(-SCREEN_WIDTH / 2) + PADDLE_DISTANCE_FROM_EDGE)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >= r_paddle.xcor() - (BALL_DIAMETER / 2) - (PADDLE_LENGTH / 2):
        ball.bounce_x()

    # Detect collision with l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() <= l_paddle.xcor() + (BALL_DIAMETER / 2) + (PADDLE_LENGTH / 2):
        ball.bounce_x()

    # Detect out of bounds right side
    if ball.xcor() >= (SCREEN_WIDTH / 2):
        ball.reset_position()
        scoreboard.l_point()
    # Detect out of bounds left side
    if ball.xcor() <= (-SCREEN_WIDTH / 2):
        ball.reset_position()
        scoreboard.r_point()

    ball.move()

screen.exitonclick()
