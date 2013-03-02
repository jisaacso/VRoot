from TemplateHandler import TemplateHandler
from models import User

class RegisterHandler(TemplateHandler):

    # regular expression to define the path
    path = r'/register'
    
    # called on HTTP POST request
    def http_get(self, properties):
        return 'view/templates/register.html', {}
    
    def http_post(self, properties):
        email =  properties.post['email']
        password = properties.post['password']
        name = properties.post['firstName']
        user = User(email=email, password=password, first_name=name)
        user.put()
        return 'view/templates/login.html', {'message': 'Account Created!<br />Please log in.'}
        