from RequestProperties import RequestProperties

class WebApp2RequestProperties(RequestProperties):
	def __init__(self, request):
		self.headers = request.headers
		self.path = request.path
		self.scheme = request.scheme
		self.get = request.GET
		self.post = request.POST
		self.cookies = request.cookies
		self.body = request.body