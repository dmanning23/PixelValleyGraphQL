from api.models.agentModel import AgentModel
from api.models.agentLocationModel import AgentLocationModel
from api.models.agentDescriptionModel import AgentDescriptionModel
from api.models.locationModel import LocationModel

def getAgentResults_resolver(obj, info, scenarioId=None, locationId=None):
    if locationId:
        agents = getLocationAgents_resolver(obj, info, locationId=locationId)
    else:
        agents = getScenarioAgents_resolver(obj, info, scenarioId)
    try:
        payload = {
            "success": True,
            "agents": agents
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getScenarioAgents_resolver(obj, info, scenarioId=None):
    #Check if this is coming from the Scenario resolver
    if obj is not None:
        scenarioId = obj["_id"]
    agentLocations = AgentLocationModel.objects(homeScenarioId=scenarioId)
    models = []
    for agentLocation in agentLocations:
        models.append(AgentModel.objects.get(id=agentLocation.agentId))
    agents = [agent.to_dict() for agent in models]
    return agents

def getScenarioOutsideAgents_resolver(obj, info, scenarioId=None):
    #Check if this is coming from the Scenario resolver
    if obj is not None:
        scenarioId = obj["_id"]
    agentLocations = AgentLocationModel.objects(homeScenarioId=scenarioId, locationId=None)
    models = []
    for agentLocation in agentLocations:
        models.append(AgentModel.objects.get(id=agentLocation.agentId))
    agents = [agent.to_dict() for agent in models]
    return agents

def getLocationAgents_resolver(obj, info, locationId=None):
    #Check if this is coming from the Location resolver
    if obj is not None:
        locationId = obj["_id"]
    agentLocations = AgentLocationModel.objects(locationId=locationId)
    models = []
    for agentLocation in agentLocations:
        models.append(AgentModel.objects.get(id=agentLocation.agentId))
    agents = [agent.to_dict() for agent in models]
    return agents

def getLocationAllAgents_resolver(obj, info, locationId=None):
    #Check if this is coming from the Location resolver
    if obj is not None:
        locationId = obj["_id"]

    #These are all the agents in the location
    agentLocations = AgentLocationModel.objects(locationId=locationId)
    models = []
    for agentLocation in agentLocations:
        models.append(AgentModel.objects.get(id=agentLocation.agentId))

    #Get all the sub locations
    subLocations = LocationModel.objects(parentLocationId=locationId)
    for subLocation in subLocations:
        agentSubLocations = AgentLocationModel.objects(locationId=subLocation.id)
        for agentSubLocation in agentSubLocations:
            models.append(AgentModel.objects.get(id=agentSubLocation.agentId))
    
    agents = [agent.to_dict() for agent in models]
    return agents

def getAgent_resolver(obj, info, id):
    try:
        model = AgentModel.objects.get(id=id)
        payload = {
            "success": True,
            "agent": model.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Agent item matching {id} not found"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getAgentDescription_resolver(obj, info, agentId=None):
    if obj is not None:
        agentId = obj["_id"]
    agentDescription = AgentDescriptionModel.objects.get(agentId=agentId)
    return  agentDescription.to_dict()