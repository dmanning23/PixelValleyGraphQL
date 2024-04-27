from api.models.plannedActivityModel import PlannedActivityModel
from api.models.agentModel import AgentModel
from api.models.scenarioModel import ScenarioModel
from api.models.agentLocationModel import AgentLocationModel
import datetime

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

def _getTodaysPlannedActivities(agentId):
     #get the scenario
    agentLocation = AgentLocationModel.objects.get(agentId=agentId)
    scenario = ScenarioModel.objects.get(id=agentLocation.currentScenarioId)

    #get the currentTime
    currentDateTime = scenario.currentDateTime;
    currentDate = datetime.datetime.combine(currentDateTime.date(), datetime.time.min)

    #Get all the planned activities, sorted by priority:
    return PlannedActivityModel.objects(agentId = agentId, day = currentDate).order_by("-priority", "+startdatetime")

def getPlannedActivities_resolver(obj, info, agentId=None):
    #Check if this is coming from the Agent resolver
    if obj is not None:
        agentId = obj["_id"]

    models = _getTodaysPlannedActivities(agentId=agentId)
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

def getCurrentPlannedActivity_resolver(obj, info, agentId=None):
        if obj is not None:
            agentId = obj["_id"]

        agentLocation = AgentLocationModel.objects.get(agentId=agentId)
        scenario = ScenarioModel.objects.get(id=agentLocation.currentScenarioId)
        currentDateTime = scenario.currentDateTime

        #Get all the planned activities, sorted by priority:
        activities = _getTodaysPlannedActivities(agentId=agentId)
        for activity in activities:
            if activity.startdatetime <= currentDateTime <= activity.enddatetime:
                return activity.to_dict()
        
        #This character is not busy right now!
        result = PlannedActivityModel()
        result.description = "Idle"
        return result.to_dict()