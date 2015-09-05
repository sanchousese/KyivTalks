from app import app, db, auth
from flask import Flask, abort, request, jsonify, g, url_for, json
from app.models import User, Place

@app.route('/')
@app.route('/index')
def index():
	return "Hello, world!"


@app.route('/api/new_user', methods = ['POST'])
def new_user():
	login = request.json.get('login')
	email = request.json.get('email')
	password = request.json.get('password')

# TODO: add normal error handling
	if (email is None) or (password is None):
		abort(400)
	if User.query.filter_by(email = email).first() is not None:
		abort(400)
	user = User(email = email, login = login)
	user.hash_password(password)
	db.session.add(user)
	db.session.commit()
	return json.dumps(user.serialize()), 201, {'Location': url_for('get_user', id = user.id, _external=True)}


@app.route('/api/users/<int:id>')
def get_user(id):
	user = User.query.get(id)
	if not user:
		abort(400)
	return json.dumps(user.serialize())


@app.route('/api/token')
@auth.login_required
def get_auth_token():
	token = g.user.generate_auth_token(600)
	return jsonify({'token': token.decode('ascii'), 'duration': 600})


@app.route('/api/resource')
@auth.login_required
def get_resource():
	return jsonify({'data': 'Hello, %s!' % g.user.login})


@app.route('/api/places')
def get_places():
	return "[ " + ", ".join(map(lambda x: str(json.dumps(x.as_dict())), Place.query.all())) + " ]"

@app.route('/api/places/<int:id>')
def get_place(id):
	place = Place.query.get(id)
	if not place:
		abort(400)
	return place.serialize()

@app.route('/api/places/new_place', methods = ['POST'])
def add_place():
	name = request.json.get('name')
	address = request.json.get('address')
	description = request.json.get('description')

	if (name is None) or (address is None):
		abort(400)
	if Place.query.filter_by(name = name).first() is not None \
	or Place.query.filter_by(address = address).first() is not None :
		abort(400)

	place = Place(name = name, address = address, description = description, rating = 0)
	db.session.add(place)
	db.session.commit()

	return json.dumps(place.serialize()), 201, {'Location': url_for('get_place', id = place.id, _external=True)}
