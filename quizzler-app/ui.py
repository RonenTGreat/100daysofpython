from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz Me")
        self.window.config(padx=30, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_body = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some Question Text",
                                                     fill='black', font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Score
        self.score_label = Label(text=f'Score: {self.quiz.score}', fg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # False Button
        false_img = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        # True Button
        true_img = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_body, text=q_text)
        else:
            self.canvas.itemconfig(self.question_body, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
