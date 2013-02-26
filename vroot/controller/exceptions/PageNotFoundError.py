from ClientError import ClientError

class PageNotFoundError(ClientError):
	def __init__(self):
		self.code = 404
		self.page = 'view/errors/404.html'
		self.dict = {}
	