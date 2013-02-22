class SubclassAware(object):
	@classmethod
	def get_subclasses(cls):
		lst = cls.__subclasses__()
		for subcls in cls.__subclasses__():
			lst += subcls.get_subclasses()
		return lst