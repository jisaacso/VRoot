from VrootHandler import VrootHandler

class ActionHandler(VrootHandler):

	path = r'ActionHandler^'
	
	def create_page(self, *args, **kwargs):
		return ''.join(args)