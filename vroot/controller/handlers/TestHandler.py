from PageHandler import PageHandler

class TestHandler(PageHandler):

	# regular expression to define the path
	path = r'/test.html'
	
	# called on HTTP GET request
	def http_get(self, properties):
	
		values = {'v1': 1, 'v2': 2, 'v3': 3, 'v4': 4}
		
		# will render views/body/test.html and views/head/test.html using values then use results in views/index.html
		return 'test.html', values
		
	# called on HTTP POST request
	def http_post(self, properties):
	
		# call superclass default function, which by default returns a 405 - Method Not Allowed
		super(TestHandler, self).http_post(properties)