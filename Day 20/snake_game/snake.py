from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __int__(self):
        self.squares = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.goto(position)
            self.squares.append(square)

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.squares[0].forward(MOVE_DISTANCE)
