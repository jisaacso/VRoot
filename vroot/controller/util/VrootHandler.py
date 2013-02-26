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
		
	def render(self, page, values):
		return VrootHandler.jinja_environment.get_template(page).render(values)
		
	def render_error(self, client_error):
		self.error(client_error.code)
		self.response.write(self.render(*client_error.template_args()))

	def render_page(self, page, values):
		
		head = ''
		try:
			head = self.render('view/pages/head/' + page, values)
		except TemplateNotFound:
			head = ''
		
		body = ''
		try:
			body = self.render('view/pages/body/' + page, values)
		except TemplateNotFound:
			self.render_error(PageNotFoundError())
			return
		
		parts = {
			'head': head,
			'body': body,
		}
		
		self.response.write(self.render('view/pages/index.html', parts))
		
		
	# helper function
	def request_properties(self):
		return WebApp2RequestProperties(self.request)
		
		
	# RequestHandler HTTP functions
	def get(self, *args, **kwargs):
		try:
			page, values = self.http_get(self.request_properties(), *args, **kwargs)
			self.render_page(page, values)
		except ClientError as e:
			self.render_error(e)
		
	def post(self, *args, **kwargs):
		try:
			page, values = self.http_post(self.request_properties(), *args, **kwargs)
			self.render_page(page, values)
		except ClientError as e:
			self.render_error(e)
		
	def head(self, *args, **kwargs):
		try:
			page, values = self.http_head(self.request_properties(), *args, **kwargs)
			self.render_page(page, values)
		except ClientError as e:
			self.render_error(e)
		
	def options(self, *args, **kwargs):
		try:
			page, values = self.http_options(self.request_properties(), *args, **kwargs)
			self.render_page(page, values)
		except ClientError as e:
			self.render_error(e)
		
	def put(self, *args, **kwargs):
		try:
			page, values = self.http_put(self.request_properties(), *args, **kwargs)
			self.render_page(page, values)
		except ClientError as e:
			self.render_error(e)
		
	def delete(self, *args, **kwargs):
		try:
			page, values = self.http_delete(self.request_properties(), *args, **kwargs)
			self.render_page(page, values)
		except ClientError as e:
			self.render_error(e)
		
	def trace(self, *args, **kwargs):
		try:
			page, values = self.http_trace(self.request_properties(), *args, **kwargs)
			self.render_page(page, values)
		except ClientError as e:
			self.render_error(e)
		
	
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