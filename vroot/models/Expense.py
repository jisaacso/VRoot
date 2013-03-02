from google.appengine.ext import db
from Event import Event
from User import User

class Expense(db.Model):
	user = db.ReferenceProperty(User)
	event = db.ReferenceProperty(Event)
	start = db.DateTimeProperty()
	end = db.DateTimeProperty()