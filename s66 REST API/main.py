from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        #Method 1.
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        #Method 2. (dictionary comprehension)
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    ### get all cafes from db and choose 1 (slower):
    # cafes = db.session.query(Cafe).all()
    # random_cafe = random.choice(cafes)
    ### get the count of cafes and select 1 (faster):
    row_count = Cafe.query.count()
    random_offset = random.randint(0, row_count - 1)
    random_cafe = Cafe.query.offset(random_offset).first()
    ### constructing the data which will be returned:
    ### https://www.adamsmith.haus/python/docs/flask.jsonify
    # return jsonify(
    #     can_take_calls=random_cafe.can_take_calls,
    #     coffee_price=random_cafe.coffee_price,
    #     has_sockets=random_cafe.has_sockets,
    #     has_toilet=random_cafe.has_toilet,
    #     has_wifi=random_cafe.has_wifi,
    #     id=random_cafe.id,
    #     img_url=random_cafe.img_url,
    #     location=random_cafe.location,
    #     map_url=random_cafe.map_url,
    #     name=random_cafe.name,
    #     seats=random_cafe.seats
    # )
    ### using the .to_dict method in the Cafe class:
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def get_all_cafes():
    cafes_rows = db.session.query(Cafe).all()
    all_cafes = [cafe.to_dict() for cafe in cafes_rows]
    return jsonify(cafes=all_cafes)

@app.route('/search')
def search_by_location():
    query_loc = request.args.get('loc')
    cafe = db.session.query(Cafe).filter_by(location=query_loc).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found in the database."}), 404
    
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    key = request.args.get('api-key')
    if key == 'TopSecretAPIKey':
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully deleted the cafe with id {cafe_id}"}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, cannot find a cafe with that id."}), 404
    else:
        return jsonify(error={"Not Allowed": "Sorry, bad api-key."})







## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True, port=8000)
