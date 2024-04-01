from api.models.itemModel import ItemModel

def getItemResults_resolver(obj, info, agentId=None, locationId=None):
    if locationId:
        items = getLocationItems_resolver(obj, info, locationId=locationId)
    else:
        items = getAgentItems_resolver(obj, info, agentId)
    try:
        payload = {
            "success": True,
            "items": items
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getAgentItems_resolver(obj, info, agentId=None):
    #Check if this is coming from the Agent resolver
    if obj is not None:
        if obj['currentItem']:
            return obj['currentItem'].to_dict()

    return None

def getLocationItems_resolver(obj, info, locationId=None):
    #Check if this is coming from the Location resolver
    if obj is not None:
        locationId = obj["_id"]
    models = ItemModel.objects(locationId=locationId)
    items = [item.to_dict() for item in models]
    return items

def getItem_resolver(obj, info, id):
    try:
        model = ItemModel.objects.get(id=id)
        payload = {
            "success": True,
            "item": model.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Item matching {id} not found"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
