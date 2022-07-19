from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)


entry = Entry(width=20)
entry.grid(column=0, row=1)

unit = Label(text="Miles")
unit.grid(column=1, row=1)

label_1 = Label(text="is equal to")
label_1.grid(column=0, row=2)

value = 0
conversion_value = Label(text=f"{value}")
conversion_value.grid(column=1, row=2)

value_unit = Label(text="Km")
value_unit.grid(column=2, row=2)










window.mainloop()
