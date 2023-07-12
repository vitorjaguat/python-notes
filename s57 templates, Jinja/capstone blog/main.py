from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    endpoint = 'https://api.npoint.io/c790b4d5cab58020d391'
    res = requests.get(endpoint)
    data = res.json()
    return render_template("index.html", posts=data)

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    endpoint = 'https://api.npoint.io/c790b4d5cab58020d391'
    res = requests.get(endpoint)
    data = res.json()
    return render_template('post.html', posts=data, id=blog_id)


if __name__ == "__main__":
    app.run(debug=True)
