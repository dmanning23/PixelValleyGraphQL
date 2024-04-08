from mongoengine import *

class AgentLocationModel(Document):
    agentId = ObjectIdField()
    homeScenarioId = ObjectIdField()
    currentScenarioId = ObjectIdField()
    locationId = ObjectIdField()

    def to_dict(self):
        return {
            "_id": self.id,
            "agentId": self.agentId,
            "homeScenarioId": self.homeScenarioId,
            "currentScenarioId": self.currentScenarioId,
            "locationId": self.locationId,
        }