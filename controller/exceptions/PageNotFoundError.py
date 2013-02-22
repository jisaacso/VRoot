from ClientError import ClientError

class PageNotFoundError(ClientError):
	def __init__(self):
		self.code = 404
		self.page = 'views/error/404.html'
		self.dict = {}
	