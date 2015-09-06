from datetime import datetime
from app import app, db, auth
from flask import Flask, abort, request, jsonify, g, url_for, json
from flask.ext.cors import CORS, cross_origin
from app.models import User, Place, Image, Rating, Comment

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
@app.route('/index')
@cross_origin()
def index():
	return "Hello, world!"


@app.route('/api/new_user', methods = ['POST'])
@cross_origin()
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
@cross_origin()
def get_user(id):
	user = User.query.get(id)
	if not user:
		abort(400)
	return json.dumps(user.serialize())


@app.route('/api/token')
@cross_origin()
@auth.login_required
def get_auth_token():
	token = g.user.generate_auth_token(600)
	return jsonify({'token': token.decode('ascii'), 'duration': 600})


@app.route('/api/resource')
@cross_origin()
@auth.login_required
def get_resource():
	return jsonify({'data': 'Hello, %s!' % g.user.login})


@app.route('/api/places')
@cross_origin()
def get_places():
	return "[ " + ", ".join(map(lambda x: str(json.dumps(x.as_dict())), Place.query.all())) + " ]"

@app.route('/api/places/<int:id>')
@cross_origin()
def get_place(id):
	place = Place.query.get(id)
	if not place:
		abort(400)
	return json.dumps(place.serialize())

@app.route('/api/places/new_place', methods = ['POST'])
@cross_origin()
@auth.login_required
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


@app.route('/api/images/new_image', methods = ['POST'])
@cross_origin()
@auth.login_required
def add_image():
	url = request.json.get('url')
	place_id = request.json.get('place_id')
	if (url is None) or (place_id is None):
		abort(400)
	if Image.query.filter_by(url = url).first() is not None:
		abort(400)
	place = Place.query.get(place_id)
	image = Image(url=url, place=place)
	db.session.add(image)
	db.session.commit()
	return jsonify({"id":image.id}), 201


@app.route('/api/images/get_by_place/<int:id>')
@cross_origin()
def get_images_by_place(id):
	for i in Place.query.filter_by(id=id):
		print i.images.all()
	# return Place.query.filter_by(id=id).images.all()
	return "bla"


@app.route('/api/ratings/new_rating', methods = ['POST'])
@cross_origin()
@auth.login_required
def add_rating():
	place_id = request.json.get('place_id')
	user_id = request.json.get('user_id')
	score = request.json.get('score')
	if (score is None) or (place_id is None) or (user_id is None):
		abort(400)
	if (Rating.query.filter_by(place_id=place_id).first() is not None) and (Rating.query.filter_by(user_id=user_id).first() is not None):
		abort(400)
	rating = Rating(user_id=user_id,place_id=place_id,score=score)
	db.session.add(rating)
	db.session.commit()
	return jsonify({"id":rating.id}), 201


@app.route('/api/comments/new_comment', methods = ['POST'])
@cross_origin()
@auth.login_required
def add_comment():
	place_id = request.json.get('place_id')
	user_id = request.json.get('user_id')
	text = request.json.get('text')
	timestamp = datetime.utcnow()
	anonimity = request.json.get('anonimity')
	if (text is None) or (place_id is None) or (user_id is None):
		abort(400)
	if anonimity:
		user_id=None
	comment = Comment(user_id=user_id,place_id=place_id,text=text, timestamp=timestamp)
	db.session.add(comment)
	db.session.commit()
	return jsonify({"id": comment.id}), 201

@app.route('/api/search_place/<string>')
@cross_origin()
def search_place(string):
	text = string.lower()
	places = []

	for i in Place.query.all():
		if text in i.name.lower() or text in i.address.lower() or text in i.description.lower():
			places.append(i)

	return "[ " + ", ".join(map(lambda x: str(json.dumps(x.as_dict())), places)) + " ]"

