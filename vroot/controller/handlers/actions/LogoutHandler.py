from controller.handlers.base import DataHandler
from models.User import User

class LogoutHandler(DataHandler):

    # regular expression to define the path
    path = r'/logout'
    
    # called on HTTP GET request
    def http_get(self, properties):
        properties.session.clear()
        return '{ "success":  true, "target": "/" }', {'type': 'json'}