from google.appengine.ext import db
from PermissionLevel import PermissionLevel

class Document(db.Model):
	name = db.StringProperty()
	path = db.StringProperty()
	read_permission = db.ReferenceProperty(PermissionLevel)
	write_permission = db.ReferenceProperty(PermissionLevel)