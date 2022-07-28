from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")
current_card = {}


# ----------------------------------------GENERATE WORD-------------------------------------
def generate_word():
    global current_card
    current_card = random.choice(words)
    word = current_card["French"]

    canvas.itemconfig(word_text, text=word)
    canvas.itemconfig(title_text, text="French")

# ----------------------------------------FLIP CARD-------------------------------------
def flip_card():
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=current_card["English"])



# ----------------------------------------UI SETUP-------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button Wrong
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, command=generate_word, highlightthickness=0)
wrong_button.grid(column=0, row=1)

# Button Right
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, command=generate_word, highlightthickness=0)
right_button.grid(column=1, row=1)
generate_word()





window.mainloop()
