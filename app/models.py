from flask import g
from app import app, db, auth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
						  as Serializer, BadSignature, SignatureExpired)


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	login = db.Column(db.String(16), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password_hash = db.Column(db.String(127))
	comments = db.relationship('Comment', backref='author', lazy='dynamic')
	ratings = db.relationship('Rating',backref='author', lazy='dynamic')

	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

	def generate_auth_token(self, expiration = 600):
		s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
		return s.dumps({'id': self.id})

	@staticmethod
	def verify_auth_token(token):
		s = Serializer(app.config['SECRET_KEY'])
		try:
			data = s.loads(token)
		except SignatureExpired:
			return None    # valid token, but expired
		except BadSignature:
			return None    # invalid token
		user = User.query.get(data['id'])
		return user


	def __repr__(self):
		return '<User %r>' % (self.login)

@auth.verify_password
def verify_password(email_or_token, password):
	# first try to authenticate by token
	user = User.verify_auth_token(email_or_token)
	if not user:
		# try to authenticate with username/password
		user = User.query.filter_by(email = email_or_token).first()
		if not user or not user.verify_password(password):
			return False
	g.user = user
	return True


class Rating(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	place_id = db.Column(db.Integer,db.ForeignKey('place.id'))
	score = db.Column(db.Integer)

	def __repr__(self):
		return '<Score %d by %d to %d>' % (self.score,self.user_id,self.place_id)


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
	place_id = db.Column(db.Integer,db.ForeignKey('place.id'))
	text = db.Column(db.String(127))
	timestamp = db.Column(db.DATETIME)
	def __repr__(self):
		return '<Comment %r by %d to %d>' % (self.text,self.user_id,self.place_id)


class Image(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
	url = db.Column(db.String(255))
	def __repr__(self):
		return '<Image of %d url %r>' % (self.place_id, self.url)


class Place(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.String(32), index=True, unique=True)
	name = db.Column(db.String(16), index=True, unique=True)
	description = db.Column(db.String(511))
	rating = db.Column(db.Integer)
	comments = db.relationship('Comment', backref='place', lazy='dynamic')
	ratings = db.relationship('Rating', backref='place', lazy='dynamic')
	images = db.relationship('Image', backref='place', lazy='dynamic')

	def __repr__(self):
		return '<Place %r by address %r with rating %r>' % (self.name,self.address,self.rating)

