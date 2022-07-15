import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

location = turtle.Turtle()
location.hideturtle()
location.penup()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
answer_state.title()

data = pandas.read_csv("50_states.csv")

state = data["state"].to_list()

if answer_state.title() in state:
    x_cor = int(data[data.state == answer_state.title()].x)
    y_cor = int(data[data.state == answer_state.title()].y)
    location.goto(x_cor, y_cor)
    location.write(f"{answer_state}")




screen.exitonclick()
