from mongoengine import *

class Article(EmbeddedDocument):

    headline = StringField()
    body = StringField()

    def to_dict(self):
        return {
            "headline": self.headline,
            "body": self.body,
        }
