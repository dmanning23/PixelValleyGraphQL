from mongoengine import *

class NewspaperModel(Document):
    meta = {'collection': 'newspaper'}
    scenarioId = ObjectIdField()
    name = StringField()
    description = StringField()
    dayOfWeek = IntField()

    def to_dict(self):
        return {
            "_id": self.id,
            "scenarioId": self.scenarioId,
            "name": self.name,
            "description": self.description,
            "dayOfWeek": self.dayOfWeek
        }

class ArticleModel(EmbeddedDocument):
    headline = StringField()
    body = StringField()

    def to_dict(self):
        return {
            "headline": self.headline,
            "body": self.body,
        }

class EditionModel(Document):
    meta = {'collection': 'edition'}
    newspaperId = ObjectIdField()
    articles = ListField(EmbeddedDocumentField(ArticleModel))
    date = DateField()

    def to_dict(self):
        return {
            "_id": self.id,
            "newspaperId": self.newspaperId,
            "date": str(self.date.strftime('%A, %B %d, %Y')),
            "articles": self.articles
        }
