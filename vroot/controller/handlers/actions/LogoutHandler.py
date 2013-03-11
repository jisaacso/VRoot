from controller.handlers.base import ActionHandler
from models.User import User

class LogoutHandler(ActionHandler):

    # regular expression to define the path
    path = r'/logout'
    
    # called on HTTP GET request
    def http_get(self, properties):
        properties.session.clear()
        return '{ "success":  true, "target": "/" }'