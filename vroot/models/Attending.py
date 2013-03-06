from google.appengine.ext import db
from User import User
from Event import Event

class Attending(db.Model):
	user = db.ReferenceProperty(User, collection_name='attending')
	event = db.ReferenceProperty(Event, collection_name='attending')