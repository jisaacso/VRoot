from google.appengine.ext import db
from User import User
from Waiver import Waiver

class UserWaiver(db.Model):
	user = db.ReferenceProperty(User, collection_name='user_waivers')
	waiver = db.ReferenceProperty(Waiver, collection_name='user_waivers')
	file = db.StringProperty()