from TemplateHandler import TemplateHandler

class IndexHandler(TemplateHandler):

	# regular expression to define the path
	path = r'/'
	
	# called on HTTP GET request
	def http_get(self, properties):
		return 'view/templates/index.html', {}