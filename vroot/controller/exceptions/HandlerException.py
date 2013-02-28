class HandlerException(Exception):
	def __init__(self, cls):
		error_text = 'Error: Handler ' + cls.__name__ + ' does not have a create_page method.'
		super(HandlerException, self).__init__(error_text)