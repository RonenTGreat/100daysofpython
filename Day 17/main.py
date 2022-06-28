from turtle import Turtle, Screen
import random
import turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

# Challenge 1: Draw a square
# for _ in range(4):
#   timmy_the_turtle.forward(100)
#   timmy_the_turtle.right(90)

# Challenge 2: Draw a dash
# for _ in range(15):
#   timmy_the_turtle.penup()
#   timmy_the_turtle.forward(10)
#   timmy_the_turtle.pendown()
#   timmy_the_turtle.forward(10)


# Challenge 3: Draw different shapes with random colours
# sides = 3
# colors = ['red', 'purple', 'cyan', 'green', 'blue']
# while sides < 11:
#   the_color = random.choice(colors)
#   timmy_the_turtle.color(the_color)
#   for _ in range(sides):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(360/sides)
#   sides += 1


# Challenge 4: Generate random walk
# timmy_the_turtle.speed('fastest')
# angle = [0, 90, 180, 270]
# colors = ['red', 'purple', 'cyan', 'green', 'blue']
# timmy_the_turtle.width(15)

# for _ in range(200):
#   timmy_the_turtle.color(random.choice(colors))
#   timmy_the_turtle.forward(30)
#   timmy_the_turtle.setheading(random.choice(angle))
  




screen = Screen()
screen.exitonclick()
