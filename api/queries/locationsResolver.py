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