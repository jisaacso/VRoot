from VrootHandler import VrootHandler

class DataHandler(VrootHandler):

	path = r'DataHandler^'
	
	def render_page(self, data, *args):
		return data