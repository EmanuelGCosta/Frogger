from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.initial_pos()

    def movimento(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def initial_pos(self):
        self.goto(STARTING_POSITION)