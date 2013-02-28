from SubclassAware import SubclassAware
from WebApp2RequestProperties import WebApp2RequestProperties
from controller.exceptions import ClientError, MethodNotAllowedError, PageNotFoundError
import webapp2
import jinja2
from jinja2 import TemplateNotFound
import os

class VrootHandler(webapp2.RequestHandler, SubclassAware):
	jinja_environment = jinja2.Environment(
		loader=jinja2.FileSystemLoader(os.getcwd()))
		
	def render_template(self, page, values):
		return VrootHandler.jinja_environment.get_template(page).render(values)
		
	def show_error(self, client_error):
		self.error(client_error.code)
		self.response.write(self.render_template(*client_error.template_args()))

	def show_page(self, *args, **kwargs):
		self.response.write(self.create_page(*args, **kwargs))
		
	def create_page(self, *args, **kwargs):
		raise HandlerException(type(self))
		
	# helper function
	def request_properties(self):
		return WebApp2RequestProperties(self.request)
		
		
	# RequestHandler HTTP functions
	def get(self, *args, **kwargs):
		try:
			render_args = self.http_get(self.request_properties(), *args, **kwargs)
			self.show_page(*render_args)
		except ClientError as e:
			self.show_error(e)
		
	def post(self, *args, **kwargs):
		try:
			render_args = self.http_post(self.request_properties(), *args, **kwargs)
			self.show_page(*render_args)
		except ClientError as e:
			self.show_error(e)
		
	def head(self, *args, **kwargs):
		try:
			render_args = self.http_head(self.request_properties(), *args, **kwargs)
			self.show_page(*render_args)
		except ClientError as e:
			self.show_error(e)
		
	def options(self, *args, **kwargs):
		try:
			render_args = self.http_options(self.request_properties(), *args, **kwargs)
			self.show_page(*render_args)
		except ClientError as e:
			self.show_error(e)
		
	def put(self, *args, **kwargs):
		try:
			render_args = self.http_put(self.request_properties(), *args, **kwargs)
			self.show_page(*render_args)
		except ClientError as e:
			self.show_error(e)
		
	def delete(self, *args, **kwargs):
		try:
			render_args = self.http_delete(self.request_properties(), *args, **kwargs)
			self.show_page(*render_args)
		except ClientError as e:
			self.show_error(e)
		
	def trace(self, *args, **kwargs):
		try:
			render_args = self.http_trace(self.request_properties(), *args, **kwargs)
			self.show_page(*render_args)
		except ClientError as e:
			self.show_error(e)
		
	
	# default action is to 405 unless overridden
	def http_get(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('GET')
		return '405.html', {'method': 'GET'}
		
	def http_post(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('POST')
		return '405.html', {'method': 'POST'}
		
	def http_head(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('HEAD')
		return '405.html', {'method': 'HEAD'}
		
	def http_options(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('OPTIONS')
		return '405.html', {'method': 'OPTIONS'}
		
	def http_put(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('PUT')
		return '405.html', {'method': 'PUT'}
		
	def http_delete(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('DELETE')
		return '405.html', {'method': 'DELETE'}
		
	def http_trace(self, properties, *args, **kwargs):
		raise MethodNotAllowedError('TRACE')
		return '405.html', {'method': 'TRACE'}
		
	# utility functions for subclasses
	def parse_args(self, arg_string):
		ret = dict()
		args = arg_string.split('&')
		for arg in args:
			temp = arg.split('=')
			dict[temp[0]] = temp[1]
		return ret