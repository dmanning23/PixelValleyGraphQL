from ariadne import convert_kwargs_to_snake_case
from api.models.scenarioModel import ScenarioModel

@convert_kwargs_to_snake_case
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