from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=285, height=100)
window.config(padx=20, pady=20)


def convert():
    value = float(entry.get()) * 1.609
    conversion_value.config(text=f"{value.__round__(2)}")


entry = Entry(width=7)
entry.grid(column=1, row=1)

unit = Label(text="Miles")
unit.grid(column=3, row=1)

label_1 = Label(text="is equal to")
label_1.grid(column=0, row=2)

conversion_value = Label(text=f"{0}")
conversion_value.grid(column=1, row=2)

value_unit = Label(text="Km")
value_unit.grid(column=2, row=2)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=3)

window.mainloop()
