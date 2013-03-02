from controller.handlers import *
from controller.exceptions import PathException
import webapp2
import logging
from models import *

mappings = dict()
for cls in VrootHandler.get_subclasses():
	# ensure handler's class variable exists and is unique
	if not hasattr(cls, 'path') or cls.path in mappings:
		err = True
		raise PathException(cls)
	mappings[cls.path] = cls

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