from google.appengine.ext import db

class PermissionLevel(db.Model):
	name = db.StringProperty()
	rank = db.IntegerProperty()