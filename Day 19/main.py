# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# screen.listen()
#
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()

nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
