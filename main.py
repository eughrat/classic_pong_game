import time
from turtle import Screen
from paddle import Paddle
from center_line import Line


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Classic Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
line = Line()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # paddle.move()






screen.exitonclick()