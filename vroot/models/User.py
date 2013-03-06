from google.appengine.ext import db
from PermissionLevel import PermissionLevel
from Region import Region

class  User(db.Model):
	# User properties
	first_name = db.StringProperty()
	last_name = db.StringProperty()
	email = db.StringProperty()
	password = db.StringProperty()
	password_salt = db.StringProperty()
	address1 = db.StringProperty()
	address2 = db.StringProperty()
	state = db.StringProperty()
	zip = db.StringProperty()
	phone_number = db.StringProperty()
	approved = db.BooleanProperty()
	permission_level = db.ReferenceProperty(PermissionLevel, collection_name='users')
	region = db.ReferenceProperty(Region, collection_name='users')
	
	#Military Service
	has_served = db.BooleanProperty()
	branch = db.StringProperty()
	occupations = db.StringProperty()
	deployments = db.StringProperty()
	highest_rank = db.StringProperty()
	years = db.IntegerProperty()
	honorable_discharge = db.BooleanProperty()
	
	#Education
	education = db.StringProperty()
	certifications = db.StringProperty()
	occupation1 = db.StringProperty()
	occupation1Time = db.IntegerProperty()
	occupation2 = db.StringProperty()
	occupation2Time = db.IntegerProperty()
	occupation3 = db.StringProperty()
	occupation3Time = db.IntegerProperty()
	occupation4 = db.StringProperty()
	occupation4Time = db.IntegerProperty()
	