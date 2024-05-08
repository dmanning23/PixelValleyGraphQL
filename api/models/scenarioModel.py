from mongoengine import *

"""
This is the main scenario object that is stored in MongoDB
"""
class ScenarioModel(Document):
    name = StringField()
    description = StringField()
    currentDateTime = DateTimeField()
    seed = StringField()
    imageFilename = StringField()

    def to_dict(self):
        return {
            "_id": self.id,
            "name": self.name,
            "description": self.description,
            "currentDateTime": str(self.currentDateTime.strftime('%I:%M %p  %A, %B %d, %Y')),
            "seed": self.seed,
            "imageFilename": self.imageFilename,
        }