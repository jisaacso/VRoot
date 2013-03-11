from controller.handlers.base import ActionHandler
from google.appengine.ext import db

class LoginHandler(ActionHandler):

	# regular expression to define the path
	path = r'/login'
	
	# called on HTTP POST request
	def http_post(self, properties):
		email = properties.post['loginEmail']
		password = properties.post['loginPassword']
		user = db.GqlQuery("SELECT __key__ FROM User " +
						"WHERE email = :1 AND password = :2",
						email, password).get()
						
		if not user:
			return '{ "success": false, "error": "Invalid email or password." }'
                
		
		properties.session['user'] = user.id()
		return '{ "success":  true, "target": "/" }'