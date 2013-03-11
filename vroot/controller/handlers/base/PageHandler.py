from controller.framework import VRootHandler
from jinja2 import TemplateNotFound

class PageHandler(VRootHandler):

	path = r'PageHandler^'
	
	def load(self, folders, part):
		return 'view/pages/' + '/'.join(folders) + '/' + part + '.html'
	
	def render_page(self, path, values, *args):
		
		head = ''
		body = ''
		
		folders = path.split('/')
		for folder in reversed(folders):
			try:
				head = self.render_template(self.load(folders, 'head'), values) + '\n' + head
			except TemplateNotFound:
				pass
			try:
				body = self.render_template(self.load(folders, 'body'), values) + '\n' + body
			except TemplateNotFound:
				pass
			folders.pop()
		
		parts = {
			'head': head,
			'body': body,
		}
		
		return self.render_template('view/pages/index.html', parts)