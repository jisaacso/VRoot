from google.appengine.ext import db

class Event(db.Model):
	name = db.StringProperty()
	description = db.StringProperty()
	location = db.StringProperty()
	start = db.DateTimeProperty()
	end = db.DateTimeProperty()