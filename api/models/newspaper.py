from mongoengine import *

class Newspaper(Document):

    name = StringField()
    description = StringField()
    scenarioId = ObjectIdField()

    def to_dict(self):
        return {
            "_id": self.id,
            "name": self.name,
            "description": self.description,
            "scenarioId": self.scenarioId,
        }