class RequestProperties(object):
	def __init__(self):
		self.headers = {}
		self.path = ''
		self.scheme = ''
		self.get = {}
		self.post = {}
		self.cookies = {}
		self.body = ''