from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper

def make_italic(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center;">Hello, World!</h1>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=500" />'

@app.route('/bye')
@make_bold
@make_italic
@make_underline
def say_bye():
    return 'Bye!'

@app.route('/username/<name>') # setting the variable name to receive and parse dynamic urls
def greet(name):
    return f'Hello there {name}!'

@app.route('/username/<name>/<int:number>') # converting the second variable to an int
def greet_with_age(name, number):
    return f"Hello {name}, you have {number + 1} new messages!"


if __name__ == "__main__": 
    app.run(debug=True)