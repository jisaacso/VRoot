from google.appengine.ext import db
from User import User
from Waiver import Waiver

class UserWaiver(db.Model):
	user = db.ReferenceProperty(User)
	waiver = db.ReferenceProperty(Waiver)
	file = db.StringProperty()