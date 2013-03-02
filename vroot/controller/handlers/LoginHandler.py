from TemplateHandler import TemplateHandler

class LoginHandler(TemplateHandler):

	# regular expression to define the path
	path = r'/login'
	
	# called on HTTP POST request
	def http_post(self, properties):
		return 'view/templates/login.html', {'name': properties.post['login'], 'password': properties.post['password']}