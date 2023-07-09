from flask import Flask
import random

app = Flask(__name__)

gif_1 = '<div style="width:480px"><iframe allow="fullscreen" frameBorder="0" height="853" src="https://giphy.com/embed/WQjNBWFJCLcCjoeHsx/video" width="480"></iframe></div>'
gif_2 = 'https://media.giphy.com/media/474sZQqrrr2VO/giphy.gif'
gif_3 = 'https://media.giphy.com/media/11aa4O4Ko73FXW/giphy.gif'
gif_4 = 'https://media.giphy.com/media/dXrm58XwMU1wY/giphy.gif'

random_number = random.randint(0,99)
print(random_number)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 99</h1>' \
            f'<img src={gif_3} />'

@app.route('/<int:user_number>')
def guess(user_number):
    global random_number
    if user_number < random_number:
        return '<h1>Too low, try again!</h1>' \
                f'{gif_1}'
    elif user_number > random_number:
        return '<h1>Too high, try again!</h1>' \
                f'<img src={gif_4} />'
    else:
        return '<h1>Congratulations!</h1>' \
                f'<img src={gif_2} />'




if __name__ == "__main__":
    app.run(debug=True)