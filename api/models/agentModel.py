from api.models.itemModel import ItemSubModel
from mongoengine import *

class AgentModel(Document):
    name = StringField()
    age = IntField()
    gender = StringField()
    description = StringField()
    currentTime = IntField()
    status = StringField()
    emoji = StringField()

    currentItem = EmbeddedDocumentField(ItemSubModel)

    #is the agent currently using the held item?
    isUsingHeldItem = BooleanField()

    timeOfLastReflection = IntField(default=0)

    def to_dict(self):
        return {
            "_id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "description": self.description,
            "currentTime": self.currentTime,
            "status": self.status,
            "emoji": self.emoji,
        }
