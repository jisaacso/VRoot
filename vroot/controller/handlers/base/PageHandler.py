from controller.framework import VRootHandler
from jinja2 import TemplateNotFound

class PageHandler(VRootHandler):

	path = r'PageHandler^'
	
	def render_page(self, page, values, *args):
		
		head = ''
		try:
			head = self.render_template('view/pages/head/' + page, values)
		except TemplateNotFound:
			head = ''
		
		body = ''
		try:
			body = self.render_template('view/pages/body/' + page, values)
		except TemplateNotFound:
			self.render_error(PageNotFoundError())
			return
		
		parts = {
			'head': head,
			'body': body,
		}
		
		return self.render_template('view/pages/index.html', parts)