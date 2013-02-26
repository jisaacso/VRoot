from ClientError import ClientError

class MethodNotAllowedError(ClientError):
	def __init__(self, method):
		self.code = 405
		self.page = 'views/error/405.html'
		self.dict = {'method': method}