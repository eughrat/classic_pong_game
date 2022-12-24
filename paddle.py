from turtle import Turtle

STARTING_POSITIONS = [(350, 0), (350, -20), (350, -40), (350, -60)]
SECOND_STARTING_POSITIONS = [(-350, 0), (-350, -20), (-350, -40), (-350, -60)]


class Paddle():

    def __init__(self):
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)


    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.goto(position)
        self.segments.append(new_segment)


class SecondPaddle(Paddle):

    def __init__(self):
        super().__init__()

    def create_paddle(self):
        for i in SECOND_STARTING_POSITIONS:
            self.add_segment(i)

