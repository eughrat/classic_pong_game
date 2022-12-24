from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.pensize(10)
        self.penup()
        self.color("white")
        self.goto(0, 290)
        self.draw_dash_line()

    def draw_dash_line(self):
        self.right(90)
        for _ in range(10):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)
