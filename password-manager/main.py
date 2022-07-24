from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data_website = website_input.get()
    data_email = email_input.get()
    data_password = password_input.get()

    if len(data_password) <= 0 or len(data_website) <= 0 or len(data_email) <= 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=data_website,
                                       message=f"These are the details entered: \nEmail: {data_email} "
                                               f"\nPassword: {data_password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{data_website} | {data_email} | {data_password} \n")

            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website input
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

# Email/Username input
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "ronenhammond@gmail.com")

# Password input
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=17)
password_input.grid(column=1, row=3)

# Generate Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
