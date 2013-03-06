from google.appengine.ext import db
from PermissionLevel import PermissionLevel

class Document(db.Model):
	name = db.StringProperty()
	path = db.StringProperty()
	read_permission = db.ReferenceProperty(PermissionLevel, collection_name='documents_read')
	write_permission = db.ReferenceProperty(PermissionLevel, collection_name='documents_write')