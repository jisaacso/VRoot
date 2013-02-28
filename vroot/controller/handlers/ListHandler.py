from DataHandler import DataHandler
import re

class ListHandler(DataHandler):

	# regular expression to define the path
	path = r'/list'
	
	# called on HTTP GET request
	def http_get(self, properties):
		temp = ["aaa", "aab", "aac", "aba", "abb", "abc", "aca", "acb", "acc",
				"baa", "bab", "bac", "bba", "bbb", "bbc", "bca", "bcb", "bcc",
				"caa", "cab", "cac", "cba", "cbb", "cbc", "cca", "ccb", "ccc"]
		
		term = ''
		if 'term' in properties.get:
			term = properties.get['term']
				
		regex = re.compile(properties.get['term'] + '.*')
		results = filter(regex.match, temp)
	
		return '["' + '", "'.join(results) + '"]'