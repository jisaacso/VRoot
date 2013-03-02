from VrootHandler import VrootHandler

class DataHandler(VrootHandler):

	path = r'DataHandler^'
	
	def create_page(self, data, *args):
		return data