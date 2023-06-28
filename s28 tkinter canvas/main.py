from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)
    label_title.config(text='Timer', fg=GREEN)
    check_marks.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label_title.config(fg=GREEN, text='Break')
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_title.config(fg=PINK, text='Break')
        count_down(short_break_sec)
    else:
        label_title.config(fg=RED, text='Work')
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✓'
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(bg=YELLOW, padx=100, pady=50)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100, 133, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1,row=1)

label_title = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
label_title.grid(column=1,row=0)

button_start = Button(text='Start', highlightbackground=YELLOW, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text='Reset', highlightbackground=YELLOW, command=reset_timer)
button_reset.grid(column=2, row=2)

check_marks = Label(fg='#65bf6c', bg=YELLOW, font=(FONT_NAME, 40))
check_marks.grid(column=1,row=3)



window.mainloop()