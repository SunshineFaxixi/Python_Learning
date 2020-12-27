from turtle import Turtle
STARTING_POINT = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_finish(self):
        return self.ycor() > 280

    def go_to_start(self):
        self.goto(STARTING_POINT)
