from controller.handlers.base import TemplateHandler
from models.User import User

class LogoutHandler(TemplateHandler):

    # regular expression to define the path
    path = r'/logout'
    
    # called on HTTP GET request
    def http_get(self, properties):
        self.session.clear()
        return 'view/templates/login.html', {}