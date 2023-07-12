from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        return f'name: {name} password: {password}'
    else:
        return 'Oooops!'


if __name__ == '__main__':
    app.run(debug=True)