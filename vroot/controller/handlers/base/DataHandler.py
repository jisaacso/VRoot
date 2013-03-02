from VrootHandler import VrootHandler

class DataHandler(VrootHandler):

	path = r'DataHandler^'
	
	def create_page(self, *args, **kwargs):
		return ''.join(args)