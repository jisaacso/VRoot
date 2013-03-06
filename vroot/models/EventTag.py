from google.appengine.ext import db
from Event import Event
from Tag import Tag

class EventTag(db.Model):
	event = db.ReferenceProperty(Event, collection_name='event_tags')
	tag = db.ReferenceProperty(Tag, collection_name='event_tags')