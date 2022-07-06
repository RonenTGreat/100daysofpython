from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} ", align=ALIGN, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()
