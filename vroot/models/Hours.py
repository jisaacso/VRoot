from google.appengine.ext import db
from User import User
from Event import Event

class Hours(db.Model):
	user = db.ReferenceProperty(User, collection_name='hours')
	event = db.ReferenceProperty(Event, collection_name='hours')
	start = db.DateTimeProperty()
	end = db.DateTimeProperty()