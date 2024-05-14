from api.models.newspaperModel import EditionModel

def getEditionsResult_resolver(obj, info, newspaperId=None):
    try:
        payload = {
            "success": True,
            "editions": getEditions_resolver(obj, info, newspaperId)
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getEditions_resolver(obj, info, newspaperId=None):
    if obj is not None:
        newspaperId = obj["_id"]
    models = EditionModel.objects(newspaperId=newspaperId)
    editions = [edition.to_dict() for edition in models]
    return editions

def getEdition_resolver(obj, info, id):
    try:
        model = EditionModel.objects.get(id=id)
        payload = {
            "success": True,
            "edition": model.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Edition matching {id} not found"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
