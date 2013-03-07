from controller.handlers.base import TemplateHandler
from models.User import User

class MockupHandler(TemplateHandler):

	# regular expression to define the path
	path = r'/(Page-\d\d?.html)'
	
	# called on HTTP GET request
	def http_get(self, properties, page):
		if self.session.get('user'):
			user = User.get_by_id(self.session.get('user'))
			return 'view/templates/' + page, {}
		else:
			return 'view/templates/SignonPage.html', {}