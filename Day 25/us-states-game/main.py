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


data = pandas.read_csv("50_states.csv")

state = data["state"].to_list()

correct_guess = []


while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in state:
        correct_guess.append(answer_state)
        x_cor = int(data[data.state == answer_state.title()].x)
        y_cor = int(data[data.state == answer_state.title()].y)
        location.goto(x_cor, y_cor)
        location.write(answer_state)
