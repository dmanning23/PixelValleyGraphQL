from mongoengine import *

class DialogueModel(EmbeddedDocument):
    agentName = StringField()
    text = StringField()

    def to_dict(self):
        return {
            "agentName": self.agentName,
            "text": self.text,
        }

class ConversationModel(Document):

    #The scenario where the chat is taking place
    scenarioId = ObjectIdField()

    #The location where the chat is taking place
    locationId = ObjectIdField()

    #The person who initiated the conversation
    initiatingAgent = ObjectIdField()

    #Why that person chose to initiate the conversation
    reasoning = StringField()

    agents = ListField(ObjectIdField())
    summary = StringField()
    dialogue = ListField(EmbeddedDocumentField(DialogueModel))

    def to_dict(self):
        return {
            "_id": self.id,
            "scenarioId": self.scenarioId,
            "locationId": self.locationId,
            "initiatingAgentId": self.initiatingAgent,
            "reasoning": self.reasoning,
            "summary": self.summary,
            "agentIds": self.agents,
            "dialogue": self.dialogue
        }
