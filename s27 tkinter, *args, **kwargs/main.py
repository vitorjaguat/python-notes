from tkinter import *

window = Tk()
window.title('My first GUI')
window.minsize(width=500, height=300)
# add padding to all widgets in the window:
window.config(padx=20, pady=20)
window.config(bg='blue')

# label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
# changing the settings of the label:
my_label['text'] = 'new text'
my_label.config(text='yet another text')

# pack the label into the screen:
# my_label.pack()

# grid layout:
my_label.grid(column=0, row=0)


# button:
def button_clicked():
    my_label['text'] = input.get()

button = Button(text='Click me', command=button_clicked)
# button.place(x=30,y=30)
button.grid(column=1, row=1)

button_2 = Button(text='New button')
button_2.grid(column=3, row=0)

# Entry component (input):
input = Entry(width=10)
# input.pack()
# print(input.get())
input.grid(column=4, row=3)



window.mainloop()

