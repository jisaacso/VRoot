from VrootHandler import VrootHandler

class ActionHandler(VrootHandler):

	path = r'ActionHandler^'
	
	def render_page(self, *args, **kwargs):
		return ''.join(args)