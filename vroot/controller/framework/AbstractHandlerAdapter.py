import webapp2
from webapp2_extras import sessions
from controller.util import WebApp2RequestProperties

class AbstractHandlerAdapter(webapp2.RequestHandler):
    def __init__(self, request, response, handler):
        self.initialize(request, response)
        self.handler = VRootHandler()
        
    def request_properties(self):
        return WebApp2RequestProperties(self.request, self.session)
    
    # RequestHandler HTTP functions
    def get(self, *args, **kwargs):
        self.handle(*self.handler.get(self.request_properties(), *args, **kwargs))
        
    def post(self, *args, **kwargs):
        self.handle(*self.handler.post(self.request_properties(), *args, **kwargs))
        
    def head(self, *args, **kwargs):
        self.handle(*self.handler.head(self.request_properties(), *args, **kwargs))
        
    def options(self, *args, **kwargs):
        self.handle(*self.handler.options(self.request_properties(), *args, **kwargs))
        
    def put(self, *args, **kwargs):
        self.handle(*self.handler.put(self.request_properties(), *args, **kwargs))
        
    def delete(self, *args, **kwargs):
        self.handle(*self.handler.delete(self.request_properties(), *args, **kwargs))
        
    def trace(self, *args, **kwargs):
        self.handle(*self.handler.trace(self.request_properties(), *args, **kwargs))
        
    def handle(self, status, response):
        self.response.set_status(status)
        self.response.write(response)
    
        
    # sessions setup
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()