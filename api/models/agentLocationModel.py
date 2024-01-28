from Models.itemModel import ItemSubModel
from mongoengine import *

class AgentLocationModel(Document):
    agentId = ObjectIdField()
    homeScenarioId = ObjectIdField()
    currentScenarioId = ObjectIdField()
    locationId = ObjectIdField()
