from api.models.conversationModel import ConversationModel
from keys import chatApiUrl
import requests

def chatRequest_mutation(obj, info, scenarioId, locationId, agentIds):
    try:
        url = f"{chatApiUrl}/chatRequest"
        data = {"scenarioId": scenarioId,
                "locationId": locationId,
                "agentIds": agentIds }

        response = requests.post(url, data=data)

        if response.status_code == 200:
            #get the conversation from the db
            model = ConversationModel.objects.get(id=response["id"])
            payload = {
                "success": True,
                "conversation": model.to_dict()
            }
        else:
            payload = {
                "success": False,
                "errors": [ f"{response.status_code}" ]
            }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

