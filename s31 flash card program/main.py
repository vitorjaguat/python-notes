from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


# new flashcard from csv
try:
     data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
     data = pandas.read_csv('data/french_words.csv')

to_learn = data.to_dict(orient='records')

french_word = random.choice(to_learn)['French']


# buttons functions:
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill='#000000')
    canvas.itemconfig(card_word, text=current_card['French'], fill='#000000')
    canvas.itemconfig(card_image, image=card_front)

    flip_timer = window.after(3000, flip_card)

def flip_card():
        canvas.itemconfig(card_title, text='English', fill='#ffffff')
        canvas.itemconfig(card_word, text=current_card['English'], fill='#ffffff')
        canvas.itemconfig(card_image, image=card_back)

def next_know():
    to_learn.remove(current_card)
    words_to_learn_dataframe = pandas.DataFrame(to_learn)
    words_to_learn_dataframe.to_csv('data/words_to_learn.csv', index=False)
    next_card()



# ----------UI----------

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card_image = canvas.create_image(400,263,image=card_front)
card_title = canvas.create_text(400,150, text='', font=('Arial', 40, 'italic'), fill='#000000')
card_word = canvas.create_text(400,263, text='', font=('Arial', 60, 'bold'), fill='#000000')
canvas.grid(column=0,row=0,columnspan=2)

image_wrong = PhotoImage(file='images/wrong.png')
image_right = PhotoImage(file='images/right.png')
button_wrong = Button(image=image_wrong, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(column=0, row=1)
button_right = Button(image=image_right, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_know)
button_right.grid(column=1, row=1)

next_card()

window.mainloop()
