from controller.util import VrootHandler
from controller.util import PathException
from controller.handlers import *
import webapp2
import logging

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
#pairs.append((r'/405.htm', VrootHandler))

app = webapp2.WSGIApplication(pairs,
                              debug=True)