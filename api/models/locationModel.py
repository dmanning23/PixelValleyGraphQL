from mongoengine import *

class LocationModel(Document):
    scenarioId = ObjectIdField()
    parentLocationId = ObjectIdField()
    canSubdivide = BooleanField()
    name = StringField()
    description = StringField()
    imageFilename = StringField()
    resizedImageFilename = StringField()
    imageInteriorFilename = StringField()
    resizedImageInteriorFilename = StringField()

    def to_dict(self):
        return {
            "_id": self.id,
            "scenarioId": self.scenarioId,
            "parentLocationId": self.parentLocationId,
            "canSubdivide": self.canSubdivide,
            "name": self.name,
            "description": self.description,
            "imageFilename": self.imageFilename,
            "resizedImageFilename": self.resizedImageFilename,
            "imageInteriorFilename": self.imageInteriorFilename,
            "resizedImageInteriorFilename": self.resizedImageInteriorFilename,
        }
