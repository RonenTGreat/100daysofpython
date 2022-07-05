from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
squares = []

for position in starting_position:
    square = Turtle("square")
    square.color("white")
    square.penup()
    square.goto(position)
    squares.append(square)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for square_num in range(len(squares) - 1, 0, -1):
        new_x = squares[square_num - 1].xcor()
        new_y = squares[square_num - 1].ycor()
        squares[square_num].goto(new_x, new_y)
    squares[0].forward(20)










screen.exitonclick()