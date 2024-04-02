from api.models.scenarioModel import ScenarioModel

def getScenarios_resolver(obj, info):
    try:
        #get the scenario from mongodb
        models = [scenario.to_dict() for scenario in ScenarioModel.objects]
        payload = {
            "success": True,
            "scenarios": models
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    
    return payload

def getScenario_resolver(obj, info, id):
    try:
        #get the scenario from mongodb
        model = ScenarioModel.objects.get(id=id)
        payload = {
            "success": True,
            "scenario": model.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Scenario item matching {id} not found"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload