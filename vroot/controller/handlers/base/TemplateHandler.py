from controller.framework import VRootHandler

class TemplateHandler(VRootHandler):

	path = r'TemplateHandler^'
	
	def render_page(self, page, values, *args):
		return self.render_template(page, values)