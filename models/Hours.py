from google.appengine.ext import db
from User import User
from Event import Event

class Hours(db.Model):
	user = db.ReferenceProperty(User)
	event = db.ReferenceProperty(Event)
	start = db.DateTimeProperty()
	end = db.DateTimeProperty()