from api.models.conversationModel import ConversationModel
#from keys import chatApiUrl
import requests
import os

def chatRequest_mutation(obj, info, scenarioId, locationId, agentIds):
    try:
        chatApiUrl = os.getenv("chatApiUrl")
        url = f"{chatApiUrl}chatRequest"
        data = {"scenarioId": scenarioId,
                "locationId": locationId,
                "agentIds": agentIds }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            #get the conversation from the db
            id = response.json()["id"]
            model = ConversationModel.objects.get(id=id)
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

def chatResponse_mutation(obj, info, conversationId, playerQuestion):
    try:
        chatApiUrl = os.getenv("chatApiUrl")
        url = f"{chatApiUrl}chatResponse"
        data = {"conversationId": conversationId,
                "playerQuestion": playerQuestion }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            payload = {
                "success": True,
                "dialogue": response.json()
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

