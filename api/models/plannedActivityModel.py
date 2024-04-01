from mongoengine import *

class PlannedActivityModel(Document):
    meta = {'collection': 'planned_activity'}
    agentId = ObjectIdField()
    day = StringField()
    startdatetime = StringField()
    enddatetime = StringField()
    description = StringField()
    starttime = StringField()
    timeframe = StringField()
    priority = IntField()

    def to_dict(self):
        return {
            "_id": self.id,
            "agentId": self.agentId,
			"day": self.day,  
            "startDateTime": self.startdatetime,
            "endDateTime": self.enddatetime,
            "description": self.description,
            "startTime": self.starttime,
            "timeFrame": self.timeframe,
            "priority": self.priority,
        }
