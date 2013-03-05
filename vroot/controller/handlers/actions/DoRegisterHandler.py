from controller.handlers.base import DataHandler
from models import User

class DoRegisterHandler(DataHandler):

    # regular expression to define the path
    path = r'/register/(\d+)/submit'
    
    def http_post(self, properties, page):
        if page == '1':
            email =  properties.post['registerEmail']
            password = properties.post['registerPassword']
            user = User(email=email, password=password)
            user.put()
            self.session['user'] = user.key().id()
            return '{ "success":  true, "target": "/register/2" }', {'type': 'json'}
        
        elif page == '2':
            user = User.get_by_id(self.session.get('user'))
            user.firstName = properties.post['firstName']
            user.lastName = properties.post['lastName']
            user.address1 = properties.post['address1']
            user.address2 = properties.post['address2']
            user.zip = properties.post['zip']
            user.state = properties.post['state']
            user.put()
            return '{ "success":  true, "target": "/register/3" }', {'type': 'json'}
        
        elif page == '3':
            return '{ "success":  true, "target": "/register/4" }', {'type': 'json'}
        
        elif page == '4':
            return '{ "success":  true, "target": "/register/5" }', {'type': 'json'}
        
        elif page == '5':
            return '{ "success":  true, "target": "/" }', {'type': 'json'}