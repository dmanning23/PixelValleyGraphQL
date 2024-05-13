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
            "dateTime": self.dateTime,
            "summary": self.summary,
            "text": self.text,
        }