from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

label_miles = Label(text='Miles')
label_miles.grid(column=2,row=0)

label_equal = Label(text='is equal to')
label_equal.grid(column=0, row=1)

label_output = Label(text='0')
label_output.grid(column=1, row=1)

label_km = Label(text='Km')
label_km.grid(column=2, row=1)


def calculate():
    input_value = float(input.get().replace(',', '.'))
    label_output['text'] = round(input_value *  1.609, 2)


button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)




window.mainloop()