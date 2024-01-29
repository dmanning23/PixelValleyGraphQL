from api.models.locationModel import LocationModel

def getLocations_resolver(obj, info, scenarioId, parentLocationId=None):
    try:
        #get the scenario from mongodb
        models = LocationModel.objects(scenarioId=scenarioId, parentLocationId=parentLocationId)
        locations = [location.to_dict() for location in models]
        payload = {
            "success": True,
            "locations": locations
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload