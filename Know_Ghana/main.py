import turtle

screen = turtle.Screen()
screen.title("Ghana Region Game")
image = "blank_ghana_regional_map.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)


screen.mainloop()
