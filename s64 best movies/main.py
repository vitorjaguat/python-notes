from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///best-movies.db"
db = SQLAlchemy()
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'
    

with app.app_context():
    db.create_all()

# with app.app_context():
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()

# with app.app_context():
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(second_movie)
#     db.session.commit()

all_movies = []


# WTForms
class RateMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5')
    review = StringField('Your Review')
    submit = SubmitField('Done')

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title')
    submit = SubmitField('Add')


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()

    # set Movie.ranking based on the movie rating:
    for i in range(len(all_movies)):
        all_movies[i].ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    if request.method == 'POST':
        movie_selected.review = form.review.data
        movie_selected.rating = float(form.rating.data)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', movie=movie_selected, form=form)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    with app.app_context():
        movie_selected = db.get_or_404(Movie, movie_id)
        db.session.delete(movie_selected)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if request.method == 'POST':
        url = "https://api.themoviedb.org/3/search/movie"
        TMDB_AUTH = os.environ.get('TMDB_AUTH')
        headers = {
            "accept": "application/json",
            "Authorization": TMDB_AUTH
        }
        params = {
            "query": form.title.data
        }
        print(form.title.data)
        response = requests.get(url, headers=headers, params=params)
        print(response)
        new_movie_data = response.json()['results']
        print(new_movie_data)
    #     new_movie = Movie(
    #         title=new_movie_data['original_title']
    #         year=new_movie_data['release_date'].split('-')[0]
    #         description=new_movie_data['overview']
    #         rating = float(form.rating.data)
    #         ranking = db.Column(db.Integer, nullable=False)
    # review = db.Column(db.String, nullable=False)
    # img_url = db.Column(db.String, nullable=False)
    #     )
        return render_template('select.html', movies=new_movie_data)
    return render_template('add.html', form=form)

@app.route('/add_from_select')
def add_from_select():
    id = request.args.get("id")
    url = "https://api.themoviedb.org/3/movie/" + id
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Y2E3ODRiYTVhMTJkODhkOGNlMzk2NDFmZDM2NzEwNiIsInN1YiI6IjYzMjM2MGI1NWE1ZWQwMDA3ZjE4YWQ0OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ETOy8R0C9aJJc8keA0o4IfXcS02Xebnl_jfVhaA6clg"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    new_movie = Movie(
        title=data['title'],
        year=data['release_date'].split('-')[0],
        img_url=f'https://image.tmdb.org/t/p/w500{data["poster_path"]}',
        description=data['overview'],
        rating=0.0,
        ranking=0,
        review='Add a review'
    )
    # with app.app_context():
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


    





if __name__ == '__main__':
    app.run(debug=True, port=8000)
