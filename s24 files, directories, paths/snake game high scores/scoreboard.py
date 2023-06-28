from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Courier'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,280)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1 
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color('white')
    #     self.write(arg='GAME OVER', align=ALIGNMENT, font=(FONT, 30, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()
