from mongoengine import *

class GoalModel(Document):
    meta = {'collection': 'goalsStream'}
    agentId = ObjectIdField()
    title = StringField()
    timeframe = StringField()
    description = StringField()

    def to_dict(self):
        return {
            "_id": self.id,
            "agentId": self.agentId,
            "title": self.title,
            "timeFrame": self.timeframe,
            "description": self.description,
        }
