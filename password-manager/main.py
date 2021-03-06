from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=30)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
