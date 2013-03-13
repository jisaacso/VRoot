from controller.handlers.base import ActionHandler
from webapp2_extras import security
from models import User

class DoRegisterHandler(ActionHandler):

    # regular expression to define the path
    path = r'/register/(\d+)/submit'
    
    def http_post(self, properties, page):
        if page == '1':
            email =  properties.post['registerEmail']
            password = security.hash_password(properties.post['registerPassword'], 'sha1')
            user = User(email=email, password=password)
            user.put()
            properties.session['user'] = user.key().id()
            return '{ "success":  true, "target": "/register/2" }'
        
        elif page == '2':
            user = User.get_by_id(properties.session.get('user'))
            user.firstName = properties.post['firstName']
            user.lastName = properties.post['lastName']
            user.address1 = properties.post['address1']
            user.address2 = properties.post['address2']
            user.zip = properties.post['zip']
            user.state = properties.post['state']
            user.put()
            return '{ "success":  true, "target": "/register/3" }'
        
        elif page == '3':
            user = User.get_by_id(properties.session.get('user'))
            
            try:
                if(properties.post['years'] != ''):
                    user.years = int(properties.post['years'])
            except ValueError:
                return '{ "success"; false, "error": "Years must be valid number" }'
            
            user.has_served = 'not_military' not in properties.post
            user.honorable_discharge = ('honorable_discharge' in properties.post and
                                        properties.post['honorable_discharge'] == 'yes')
            user.branch = properties.post['service_name']
            user.duty_status = properties.post['duty_status']
            user.occupations = properties.post['occupations']
            user.deployments = properties.post['deployments']
            user.highest_rank = properties.post['highest_rank']
            user.put()
            return '{ "success":  true, "target": "/register/4" }'
        
        elif page == '4':
            user = User.get_by_id(properties.session.get('user'))
            try:
                if(properties.post['occupation1_time'] != ''):
                    user.occupation1Time = int(properties.post['occupation1_time'])
                if(properties.post['occupation2_time'] != ''):
                    user.occupation2Time = int(properties.post['occupation2_time'])
                if(properties.post['occupation3_time'] != ''):
                    user.occupation3Time = int(properties.post['occupation3_time'])
                if(properties.post['occupation4_time'] != ''):
                    user.occupation4Time = int(properties.post['occupation4_time'])
            except ValueError:
                return '{ "success"; false, "error": "Years must be valid number" }'
            
            user.education = properties.post['education']
            user.certifications = properties.post['certifications']
            user.occupation1 = properties.post['occupation1']
            user.occupation2 = properties.post['occupation2']
            user.occupation3 = properties.post['occupation3']
            user.occupation4 = properties.post['occupation4']
            user.put()
            return '{ "success":  true, "target": "/register/5" }'
        
        elif page == '5':
            return '{ "success":  true, "target": "/" }'