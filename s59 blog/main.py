from flask import Flask, render_template
import requests

endpoint = 'https://api.npoint.io/c790b4d5cab58020d391'
res = requests.get(endpoint)
data = res.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/posts/<int:id>')
def get_post(id):
    post_data = [post for post in data if post['id'] == id][0]
    return render_template('post.html', post=post_data)



if __name__ == "__main__":
    app.run(debug=True)