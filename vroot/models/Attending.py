from google.appengine.ext import db
from User import User
from Event import Event

class Attending(db.Model):
	user = db.ReferenceProperty(User)
	event = db.ReferenceProperty(Event)