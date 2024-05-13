from mongoengine import *
from models.article import Article

class Edition(Document):

    newspaperId = ObjectIdField()
    articles = ListField(EmbeddedDocumentField(Article))
    date = DateField()

    def to_dict(self):
        return {
            "_id": self.id,
            "newspaperId": self.newspaperId,
            "articles": self.articles,
            "date": self.date,
        }