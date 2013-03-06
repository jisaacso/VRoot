from google.appengine.ext import db
from Event import Event
from User import User

class Expense(db.Model):
	user = db.ReferenceProperty(User, collection_name='expenses')
	event = db.ReferenceProperty(Event, collection_name='expenses')
	start = db.DateTimeProperty()
	end = db.DateTimeProperty()