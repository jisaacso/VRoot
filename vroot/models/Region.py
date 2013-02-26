from google.appengine.ext import db

class Region(db.Model):
	name = db.StringProperty()