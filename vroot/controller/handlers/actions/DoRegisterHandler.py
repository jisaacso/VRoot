from controller.handlers.base import DataHandler
from models import User

class DoRegisterHandler(DataHandler):

    # regular expression to define the path
    path = r'/register/submit'
    
    def http_post(self, properties):
        email =  properties.post['email']
        password = properties.post['password']
        name = properties.post['firstName']
        user = User(email=email, password=password, first_name=name)
        user.put()
        return '{ "success":  true, "target": "/" }', {'type': 'json'}