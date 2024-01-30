from mongoengine import *

class AgentDescriptionModel(Document):

    hair = StringField()
    eyes = StringField()
    clothing = ListField()
    distinguishingFeatures = ListField()
    agentId = ObjectIdField()

    portraitFilename = StringField()
    iconFilename = StringField()
    resizedIconFilename = StringField()
    chibiFilename = StringField()
    resizedChibiFilename = StringField()

    def to_dict(self):
        return {
            "_id": self.id,
            "agentId": self.agentId,
            "portraitFilename": self.portraitFilename,
            "iconFilename": self.iconFilename,
            "resizedIconFilename": self.resizedIconFilename,
            "chibiFilename": self.chibiFilename,
            "resizedChibiFilename": self.resizedChibiFilename,
        }