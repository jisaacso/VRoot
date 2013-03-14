from controller.handlers.base import TemplateHandler
from models.User import User
from controller.exceptions import PageNotFoundError

class MockupHandler(TemplateHandler):

	# regular expression to define the path
	path = r'/Page-(\d+).html'
	
	# called on HTTP GET request
	def http_get(self, properties, page):
		if 'user' in properties.session:
			user = User.get_by_id(properties.session['user'])
			
			img = ''
			if page == '0':
				img = 'landing.png'
			elif page == '1':
				img = 'MyPage.png'
			elif page == '2':
				img = 'messegeboard.png'
			elif page == '3':
				img = 'Vevents.png'
			elif page == '4':
				img = 'AdminPersonnel.png'
			elif page == '5':
				img = 'Documentation.png'
			elif page == '6':
				img = 'untitledAdminAlerts.png'
			elif page == '7':
				img = 'AdminEvent.png'
			elif page == '8':
				img = 'AdminMessage.png'
			elif page == '9':
				img = 'SetUsrPriv.png'
			elif page == '10':
				img = 'AdminNims1.png'
			elif page == '11':
				img = 'AdminNims2.png'
			elif page == '12':
				img = 'AdminNims3.png'
			elif page == '13':
				img = 'AdminNims4.png'
			elif page == '14':
				img = 'Commute1.png'
			elif page == '15':
				img = 'Commute2.png'
			elif page == '16':
				img = 'Commute3.png'
			elif page == '17':
				img = 'VEvents1.png'
			elif page == '18':
				img = 'landing.png'
			elif page == '19':
				img = 'eventsignup.png'
			elif page == '20':
				img = 'msgboard.png'
			elif page == '21':
				img = 'personnel2.png'
			else:
				raise PageNotFoundError()
			
			return 'view/templates/Page-0.html', {'image': img,}
		else:
			return 'view/templates/SignonPage.html', {}