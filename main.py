import time
from turtle import Screen
from paddle import Paddle
from center_line import Line


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Classic Pong Game")
screen.tracer(0)

paddle = Paddle()
line = Line()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # paddle.move()






screen.exitonclick()