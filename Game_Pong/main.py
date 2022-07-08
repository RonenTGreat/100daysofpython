from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()

screen.listen()


screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
