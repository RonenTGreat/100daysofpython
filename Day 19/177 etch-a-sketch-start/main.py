from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def counter_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def reset():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="d", fun=counter_clockwise)
screen.onkey(key="c", fun=reset)
screen.exitonclick()
