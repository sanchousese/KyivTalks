from app import app

@app.route('/')
@app.route('/index')
def index():
	return "Hello, world!"


@app.route('/api/users', methods = ['POST'])
def new_user():
	email = request.json.get('username')
	password = request.json.get('password')

	if (email is None) or (password is None):
		abort(400)
	if User.query.filter_by(email = email).first() is not None:
		abort(400)
	user = User(email = email)
	user.hash_password(password)
	db.session.add(user)
	db.session.commit()
	return jsonify({ 'login': user.login }), 201, {'Location': url_for('get_user', id = user.id, _external=True)}