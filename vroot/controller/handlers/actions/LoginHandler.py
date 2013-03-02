from controller.handlers.base import DataHandler
from google.appengine.ext import db

class LoginHandler(DataHandler):

	# regular expression to define the path
	path = r'/login'
	
	# called on HTTP POST request
	def http_post(self, properties):
		email = properties.post['email']
		password = properties.post['password']
		user = db.GqlQuery("SELECT * FROM User " +
						"WHERE email = :1 AND password = :2",
						email, password).get()
						
		if not user:
			return "", {"type": "raw"}
                
		
		self.session['user'] = user.key().id()
		return "/", {"type": "raw"}