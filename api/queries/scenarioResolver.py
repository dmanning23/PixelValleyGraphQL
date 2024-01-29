from api.models.scenarioModel import ScenarioModel

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