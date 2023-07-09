from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain): #the quiz_brain parameter is of type QuizBrain
        self.quiz = quiz_brain #receiving the quiz_brain instance to be able to call its properties and methods

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0

        self.label_score = Label(text=f"Score: {self.score}", fg='white', bg=THEME_COLOR)
        self.label_score.grid(column=1, row=0)

        self.canvas = Canvas(bg='white', height=250, width=300)
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text='Some question text', 
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        image_true = PhotoImage(file='images/true.png')
        image_false = PhotoImage(file='images/false.png')

        self.button_true = Button(image=image_true, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(column=0, row=2)

        self.button_false = Button(image=image_false, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg='gray')
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz. Your score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.button_false.config(state='disabled')
            self.button_true.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        bg_color = 'green' if is_right else 'red'
        self.canvas.config(bg=bg_color)
        
        self.window.after(1000, self.get_next_question)