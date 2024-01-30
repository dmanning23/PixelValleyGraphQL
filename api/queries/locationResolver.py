from api.models.locationModel import LocationModel

def getLocationResults_resolver(obj, info, scenarioId=None, parentLocationId=None):
    try:
        payload = {
            "success": True,
            "locations": getLocations_resolver(obj, info, scenarioId, parentLocationId)
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getLocations_resolver(obj, info, scenarioId=None, parentLocationId=None):
    #Check if this is coming from the Scenario resolver
    if obj is not None:
        scenarioId = obj["_id"]
    models = LocationModel.objects(scenarioId=scenarioId, parentLocationId=parentLocationId)
    locations = [location.to_dict() for location in models]
    return locations

def getLocation_resolver(obj, info, id):
    try:
        #get the scenario from mongodb
        model = LocationModel.objects.get(id=id)
        payload = {
            "success": True,
            "location": model.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Location item matching {id} not found"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload