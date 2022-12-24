from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, start_position):
        super().__init__()
        self.start_position = start_position
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.start_position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
