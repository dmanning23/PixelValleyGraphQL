from api.models.plannedActivityModel import PlannedActivityModel

def getPlannedActivityResults_resolver(obj, info, agentId=None):

    try:
        payload = {
            "success": True,
            "plannedActivities": getPlannedActivities_resolver(obj, info, agentId=agentId)
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getPlannedActivities_resolver(obj, info, agentId=None):
    #Check if this is coming from the Agent resolver
    if obj is not None:
        agentId = obj["_id"]
    models = PlannedActivityModel.objects(agentId=agentId)
    plannedActivities = [plannedActivity.to_dict() for plannedActivity in models]
    return plannedActivities

def getPlannedActivity_resolver(obj, info, id):
    try:
        model = PlannedActivityModel.objects.get(id=id)
        payload = {
            "success": True,
            "plannedActivity": model.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["PlannedActivity matching {id} not found"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
