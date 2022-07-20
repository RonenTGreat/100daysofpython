import turtle
import pandas
screen = turtle.Screen()
screen.title("Ghana Region Game")
image = "blank_ghana_regional_map.gif"
screen.addshape(image)
turtle.shape(image)

location = turtle.Turtle()
location.hideturtle()
location.penup()

data = pandas.read_csv("16_regions.csv")
regions = data["region"].to_list()

correct_guess = []

while len(correct_guess) < 16:
    answer = screen.textinput(title=f"{len(correct_guess)}/16 Guess the Region",
                              prompt="What's another region's name").title()

    if answer == "Exit":
        missing_regions = [region for region in regions if region not in correct_guess]
        learn = pandas.DataFrame(missing_regions)
        learn.to_csv("regions_to_learn.csv")
        break
    if answer in regions:
        correct_guess.append(answer)
        location.goto(int(data[data.region == answer.title()].x), int(data[data.region == answer.title()].y))
        location.write(answer)

