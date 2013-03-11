from controller.util import SubclassAware
from controller.framework import WebApp2RequestProperties
from controller.exceptions import ClientError, MethodNotAllowedError, PageNotFoundError
import jinja2
from jinja2 import TemplateNotFound
import os

class VRootHandler(SubclassAware):
	jinja_environment = jinja2.Environment(
		loader=jinja2.FileSystemLoader(os.getcwd()))
		
	def render_template(self, page, values):
		return VRootHandler.jinja_environment.get_template(page).render(values)
		
	def show_error(self, client_error):
		try:
			return self.render_template(*client_error.template_args())
		except TemplateNotFound as e:
			return "Meta 404: Error page not found"
		
	def render_page(self, *args):
		raise HandlerException(type(self))
		
		
	# RequestHandler HTTP functions
	def get(self, request_properties, *args, **kwargs):
		try:
			render_args = self.http_get(request_properties, *args, **kwargs)
			return 200, self.render_page(*render_args)
		except ClientError as e:
			return e.code, self.render_error(e)
		except TemplateNotFound as e:
			return 404, self.render_error(PageNotFoundError())
		
	def post(self, request_properties, *args, **kwargs):
		try:
			render_args = self.http_post(request_properties, *args, **kwargs)
			return 200, self.render_page(*render_args)
		except ClientError as e:
			return e.code, self.render_error(e)
		except TemplateNotFound as e:
			return 404, self.render_error(PageNotFoundError())
		
	def head(self, request_properties, *args, **kwargs):
		try:
			render_args = self.http_head(request_properties, *args, **kwargs)
			return 200, self.render_page(*render_args)
		except ClientError as e:
			return e.code, self.render_error(e)
		except TemplateNotFound as e:
			return 404, self.render_error(PageNotFoundError())
		
	def options(self, request_properties, *args, **kwargs):
		try:
			render_args = self.http_options(request_properties, *args, **kwargs)
			return 200, self.render_page(*render_args)
		except ClientError as e:
			return e.code, self.render_error(e)
		except TemplateNotFound as e:
			return 404, self.render_error(PageNotFoundError())
		
	def put(self, request_properties, *args, **kwargs):
		try:
			render_args = self.http_put(request_properties, *args, **kwargs)
			return 200, self.render_page(*render_args)
		except ClientError as e:
			return e.code, self.render_error(e)
		except TemplateNotFound as e:
			return 404, self.render_error(PageNotFoundError())
		
	def delete(self, request_properties, *args, **kwargs):
		try:
			render_args = self.http_delete(request_properties, *args, **kwargs)
			return 200, self.render_page(*render_args)
		except ClientError as e:
			return e.code, self.render_error(e)
		except TemplateNotFound as e:
			return 404, self.render_error(PageNotFoundError())
		
	def trace(self, request_properties, *args, **kwargs):
		try:
			render_args = self.http_trace(request_properties, *args, **kwargs)
			return 200, self.render_page(*render_args)
		except ClientError as e:
			return e.code, self.render_error(e)
		except TemplateNotFound as e:
			return 404, self.render_error(PageNotFoundError())
		
	
	# default action is to 405 unless overridden
	def http_get(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('GET')
		
	def http_post(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('POST')
		
	def http_head(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('HEAD')
		
	def http_options(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('OPTIONS')
		
	def http_put(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('PUT')
		
	def http_delete(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('DELETE')
		
	def http_trace(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('TRACE')