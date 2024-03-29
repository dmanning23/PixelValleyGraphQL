
from api.models.itemModel import ItemModel
from api.models.goalModel import GoalModel
from api.models.locationModel import LocationModel
from api.models.agentModel import AgentModel

def getGoalResults_resolver(obj, info, agentId=None):
    if agentId:
        goals = getAgentGoals_resolver(obj, info, agentId=agentId)
    
    try:
        payload = {
            "success": True,
            "goals": goals
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getAgentGoals_resolver(obj, info, agentId=None):
    #Check if this is coming from the Agent resolver
    if obj is not None:
        agentId = obj["_id"]
    models = GoalModel.objects(agentId=agentId)
    goals = [goal.to_dict() for goal in models]
    return goals

def getGoal_resolver(obj, info, id):
    try:
        model = GoalModel.objects.get(id=id)
        payload = {
            "success": True,
            "goal": model.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Goal matching {id} not found"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
