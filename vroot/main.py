from controller.framework import VRootHandler
from controller.handlers import *
from controller.exceptions import PathException
import webapp2
from controller.framework import AbstractHandlerAdapter

def get_adapter(cls):
	class ConcreteHandlerAdapter(AbstractHandlerAdapter):
		def __init__(self, request, response):
			self.initialize(request, response)
			self.handler = cls()
	return ConcreteHandlerAdapter

mappings = dict()
for cls in VRootHandler.get_subclasses():
	# ensure handler's class variable exists and is unique
	if not hasattr(cls, 'path') or cls.path in mappings:
		err = True
		raise PathException(cls)
	mappings[cls.path] = get_adapter(cls)

# build tuple list for instantiating WSGIApplication
pairs = list()
for path, cls in mappings.items():
	pairs.append((path, cls))
		
	
# set configuration
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'shrim',
}

app = webapp2.WSGIApplication(pairs, config=config,
                              debug=True)