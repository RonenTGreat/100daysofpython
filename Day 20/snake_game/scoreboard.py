from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highest_score} ", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.update_score()

    def increase(self):
        self.score += 1
        self.update_score()
