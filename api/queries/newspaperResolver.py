from api.models.newspaperModel import NewspaperModel

def getNewspaperResults_resolver(obj, info, scenarioId=None):
    try:
        payload = {
            "success": True,
            "newspapers": getNewspapers_resolver(obj, info, scenarioId)
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getNewspapers_resolver(obj, info, scenarioId=None):
    if obj is not None:
        scenarioId = obj["_id"]
    models = NewspaperModel.objects(scenarioId=scenarioId)
    newspapers = [newspaper.to_dict() for newspaper in models]
    return newspapers

def getNewspaper_resolver(obj, info, id):
    try:
        model = NewspaperModel.objects.get(id=id)
        payload = {
            "success": True,
            "newspaper": model.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Newspaper matching {id} not found"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
