from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

@app.route('/')
def home(): 
    random_number = random.randint(1,10)
    year = dt.datetime.now().year
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')
def guess(name: str):
    age_endpoint = 'https://api.agify.io?name=' + name.lower()
    age_res = requests.get(age_endpoint)
    age = age_res.json()['age']

    gender_endpoint = 'https://api.genderize.io?name=' + name.lower()
    gender_res = requests.get(gender_endpoint)
    gender = gender_res.json()['gender']

    return render_template('guess.html',name=name, age=age, gender=gender)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    api_endpoint = 'https://api.npoint.io/c790b4d5cab58020d391'
    res = requests.get(api_endpoint)
    data = res.json()
    return render_template('blog.html', posts=data)

if __name__ == '__main__':
    app.run(debug=True)