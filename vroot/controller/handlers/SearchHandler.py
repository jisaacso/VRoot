from PageHandler import PageHandler

class SearchHandler(PageHandler):

	# regular expression to define the path
	path = r'/search'
	
	# called on HTTP GET request
	def http_get(self, properties):
	
		values = {}
		
		# will render views/body/test.html and views/head/test.html using values then use results in views/index.html
		return 'search.html', values
		
	# called on HTTP POST request
	def http_post(self, properties):
	
		# call superclass default function, which by default returns a 405 - Method Not Allowed
		super(TestHandler, self).http_post(properties)