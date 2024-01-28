from ariadne import convert_kwargs_to_snake_case
from api.models.scenarioModel import ScenarioModel

@convert_kwargs_to_snake_case
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