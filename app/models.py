from app import db
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	login = db.Column(db.String(16), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password_hash = db.Column(db.String(128))

	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

	def __repr__(self):
		return '<User %r>' % (self.login)
