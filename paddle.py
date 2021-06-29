from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.setpos(position)
        self.penup()
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)


