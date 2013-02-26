from google.appengine.ext import db
from Event import Event
from Tag import Tag

class EventTag(db.Model):
	event = db.ReferenceProperty(Event)
	tag = db.ReferenceProperty(Tag)