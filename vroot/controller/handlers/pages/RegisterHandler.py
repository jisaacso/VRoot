from controller.handlers.base import TemplateHandler
from models import User

class RegisterHandler(TemplateHandler):

    # regular expression to define the path
    path = r'/register/(\d)'
    
    # called on HTTP GET request
    def http_get(self, properties, page):
        return "view/templates/register"+ page + ".html", {}
        