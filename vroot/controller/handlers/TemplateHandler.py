from controller.util import VrootHandler
from jinja2 import TemplateNotFound

class TemplateHandler(VrootHandler):

	path = r'TemplateHandler^'
	
	def create_page(self, page, values, *args, **kwargs):
		return self.render_template(page, values)