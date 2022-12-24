import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from center_line import Line

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Classic Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
line = Line()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # DETECT COLLISION WITH BORDER
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#     DETECT COLLISION WITH r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320 :
        ball.bounce_x()

    if ball.xcor() > 380 or ball.xcor() < - 380:
        ball.reset_position()


screen.exitonclick()
