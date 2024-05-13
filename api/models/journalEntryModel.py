from mongoengine import *

class JournalEntryModel(Document):
    agentId = ObjectIdField()
    dateTime = DateTimeField()
    summary = StringField()
    text = StringField()

    def to_dict(self):
        return {
            "_id": self.id,
            "agentId": self.agentId,
            "dateTime": str(self.dateTime.strftime('%A, %B %d, %Y')),
            "summary": self.summary,
            "text": self.text,
        }