from google.appengine.ext import db

class Tag(db.Model):
	name = db.StringProperty()