from turtle import Turtle

STARTING_POSITION = (350, 0)
SECOND_STARTING_POSITION = (-350, 0)
MOVE_DISTANCE = 20

class Paddle():

    def __init__(self):
        self.paddle = Turtle()
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(STARTING_POSITION)

    def up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)


