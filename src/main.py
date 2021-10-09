"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Vehicles, Starships
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    users = User.query.all()
    all_users = list(map(lambda user: user.serialize(), users))
    
    return jsonify(all_users), 200

@app.route('/characters', methods=['GET'])
def get_people():
    characters = Characters.query.all()
    all_characters= list(map(lambda person: person.serialize(), characters))

    return jsonify(all_people), 200

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_single_people():
    single_character = Characters.query.get(character_id)

    return jsonify(single_character), 200

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicles.query.all()
    all_vehicles = list(map(lambda vehicle: vehicle.serialize(), vehicles))

    return jsonify(all_vehicles), 200

@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_single_vehicle():
    single_vehicle = Vehicles.query.get(vehicle_id)

    return jsonify(single_vehicle), 200


@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    all_planets = list(map(lambda planet: planet.serialize(), planets))

    return jsonify(all_vehicles), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_single_planet():
    single_planet = Planets.query.get(planet_id)

    return jsonify(single_planet), 200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
