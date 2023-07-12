from flask import Flask, render_template, request
import requests
import smtplib
import os

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

my_email = 'jaguattt@gmail.com'
pw_app = os.environ.get('GMAIL_APPPW')

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name, email, phone, message)
        # send email:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=pw_app)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs='vitorbutkus@gmail.com', 
                msg=f"Subject:Message from Contact Form\n\n{message}")
        return render_template('contact.html', success_msg='Successfully sent message.')
    elif request.method == 'GET':
        return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
