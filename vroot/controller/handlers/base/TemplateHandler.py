from VrootHandler import VrootHandler
from jinja2 import TemplateNotFound

class TemplateHandler(VrootHandler):

	path = r'TemplateHandler^'
	
	def render_page(self, page, values, *args):
		return self.render_template(page, values)