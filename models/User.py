from google.appengine.ext import db
from PermissionLevel import PermissionLevel
from Region import Region

class  User(db.Model):
	first_name = db.StringProperty()
	last_name = db.StringProperty()
	email = db.StringProperty()
	password = db.StringProperty()
	password_salt = db.StringProperty()
	address = db.StringProperty()
	state = db.StringProperty()
	zip = db.IntegerProperty()
	phone_number = db.StringProperty()
	approved = db.BooleanProperty()
	permission_level = db.ReferenceProperty(PermissionLevel)
	region = db.RefernceProperty(Region)