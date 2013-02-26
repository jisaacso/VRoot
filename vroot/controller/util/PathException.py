class PathException(Exception):
	def __init__(self, cls):
		error_text = 'Error: Class ' + cls.__name__ + ' either does not have a path or uses one identical to another class'
		super(PathException, self).__init__(error_text)