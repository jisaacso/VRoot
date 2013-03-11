from controller.framework import VRootHandler

class ActionHandler(VRootHandler):

	path = r'ActionHandler^'
	
	def render_page(self, *args, **kwargs):
		return ''.join(args)