from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 40, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.left_score}", align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.right_score}", align=ALIGN, font=FONT)

    def l_point(self):
        self.left_score += 1
        self.update_score()

    def r_point(self):
        self.right_score += 1
        self.update_score()


