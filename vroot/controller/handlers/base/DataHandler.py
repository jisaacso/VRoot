from controller.framework import VRootHandler

class DataHandler(VRootHandler):

	path = r'DataHandler^'
	
	def render_page(self, data, *args):
		return data