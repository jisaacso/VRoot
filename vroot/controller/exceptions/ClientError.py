class ClientError(Exception):
	def __init__(self, code, title, detail):
		self.code = code
		self.page = "view/errors/4xx.html"
		self.dict = {"code": code, "title": title, "detail": detail}
		
	def  template_args(self):
		return self.page, self.dict