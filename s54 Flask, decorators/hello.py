from flask import Flask

app = Flask(__name__)

@app.route('/') # this decoration adds a condition: only run this code if the user hits the '/' route
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'Bye!'


if __name__ == "__main__": # rodar apenas se for um script principal, não como um módulo
    app.run()