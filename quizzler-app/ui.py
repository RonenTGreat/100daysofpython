from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_body = self.canvas.create_text(150, 125, text="Some annoying text here because I'm tired.",
                                                     fill='black', font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=0, columnspan=2)

        # False Button
        self.false_img = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=self.false_img)
        self.false_button.grid(column=1, row=2)

        # True Button
        self.true_img = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=self.true_img)
        self.true_button.grid(column=0, row=2)

        self.window.mainloop()
