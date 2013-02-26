from google.appengine.ext import db
from Region import Region
from PermissionLevel import PermissionLevel

class Waiver(db.Model):
	name = db.StringProperty()
	file = db.StringProperty()
	region = db.ReferenceProperty(Region)
	min_permission = db.ReferenceProperty(PermissionLevel)