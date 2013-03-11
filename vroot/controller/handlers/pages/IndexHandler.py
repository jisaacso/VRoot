from controller.handlers.base import TemplateHandler
from models.User import User

class IndexHandler(TemplateHandler):

	# regular expression to define the path
	path = r'/'
	
	# called on HTTP GET request
	def http_get(self, properties):
		if 'user' in properties.session:
			user = User.get_by_id(properties.session['user'])
			return 'view/templates/Page-0.html', {'name': user.first_name}
		else:
			return 'view/templates/SignonPage.html', {}
