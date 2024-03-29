from mongoengine import *
from api.models.finiteStateMachineModel import FiniteStateMachineModel

class BaseItemModel():
    name = StringField()
    description = StringField()
    canInteract = BooleanField()
    canBePickedUp = BooleanField()
    stateMachine = EmbeddedDocumentField(FiniteStateMachineModel)

    #This will be populated if the item is in a location
    locationId = ObjectIdField()

    #This will be populated if an item is being used by the character
    usingCharacterId = ObjectIdField()

    status = StringField()
    emoji = StringField()

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "canInteract": self.canInteract,
            "canBePickedUp": self.canBePickedUp,
            #"stateMachine": self.stateMachine,
            "locationId": self.locationId,
            "usingCharacterId": self.usingCharacterId,
            "status": self.status,
            "emoji": self.emoji,
        }

class ItemModel(BaseItemModel, Document):
    def to_dict(self):
        return BaseItemModel.to_dict(self) | {"_id": self.id,}

class ItemSubModel(BaseItemModel, EmbeddedDocument):
    def to_dict(self):
        return BaseItemModel.to_dict(self)