from google.appengine.ext import db

class Expense(db.Model):
	user = db.ReferenceProperty(User)
	event = db.ReferenceProperty(Event)
	start = db.DateTimeProperty()
	end = db.DateTimeProperty()