from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Courier'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,280)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.text = f'Score: {self.score}'
        self.write(arg=self.text, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1 
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color('white')
        self.write(arg='GAME OVER', align=ALIGNMENT, font=(FONT, 30, 'normal'))