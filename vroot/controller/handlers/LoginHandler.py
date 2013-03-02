from TemplateHandler import TemplateHandler
from google.appengine.ext import db

class LoginHandler(TemplateHandler):

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
			return 'view/templates/login.html', {'message': 'Invalid Username or Password.<br /> Please try again.'}
                
		
		self.session['user'] = user.key().id()
		return 'view/templates/index.html', {'name': user.first_name}