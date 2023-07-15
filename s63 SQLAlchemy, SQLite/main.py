from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


############### managing db using SQLAlchemy: ##########

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# create the extension
db = SQLAlchemy()

# initialize the app with the extension
db.init_app(app)

# define model:
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating=db.Column(db.Float, nullable=False)

     # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# with app.app_context():
#     first_book = Book(
#         id=1,
#         title='O Alienista',
#         author='Machado de Assis',
#         rating='9.1'
#     )
#     db.session.add(first_book)
#     db.session.commit()


all_books = []




@app.route('/')
def home():
    # Read all records:
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        newBook = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
        )
        with app.app_context():
            db.session.add(newBook)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_edit = db.get_or_404(Book, book_id)
        book_to_edit.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template('edit.html', book=book_selected)

@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    with app.app_context():
        book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True, port=8000)



# Create a New Database
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
 
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///<name of database>.db"
# db = SQLAlchemy()
# db.init_app(app)


# Create a New Table
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     rating = db.Column(db.Float, nullable=False
 
# with app.app_context():
#     db.create_all()


# In addition to these things, the most crucial thing to figure out when working with any new database technology is how to CRUD data records.

# Create

# Read

# Update

# Delete



# So, let's go through each of these using SQLite and SQLAlchemy:



# Create A New Record
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()
# NOTE: When creating new records, the primary key fields is optional. you can also write:

# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)

# the id field will be auto-generated.



# Read All Records
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()
# To read all the records we first need to create a "query" to select things from the database. When we execute a query during a database session we get back the rows in the database (a Result object). We then use scalars() to get the individual elements rather than entire rows.





# Read A Particular Record By Query
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
# To get a single element we can use scalar() instead of scalars().



# Update A Particular Record By Query
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit() 


# Update A Record By PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)  
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()  
# Flask-SQLAlchemy also has some handy extra query methods like get_or_404() that we can use. Since Flask-SQLAlchemy version 3.0 the previous query methods like Book.query.get() have been deprecated



# Delete A Particular Record By PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
# You can also delete by querying for a particular value e.g. by title or one of the other properties. Again, the get_or_404() method is quite handy.





############### managing db directly with sqlite3: ############
# crate db:
# db = sqlite3.connect('books-collection.db')

# create cursor:
# cursor = db.cursor()

# create table:
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# insert some data:
# cursor.execute("INSERT INTO books VALUES(1, 'O Abacateiro', 'Maria Josefa', '8.7')")

# commit into the db:
# db.commit()

# (with SQLAlchemy we don't have to write SQL syntax!)




