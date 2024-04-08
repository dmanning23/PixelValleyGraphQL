from api.models.conversationModel import ConversationModel

def getConversationResults_resolver(obj, info, agentId=None):
    try:
        payload = {
            "success": True,
            "conversations": getConversations_resolver(obj, info, agentId)
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getConversations_resolver(obj, info, agentId=None):
    #TODO: add paging to this resolver
    if obj is not None:
        agentId = obj["_id"]
    models = ConversationModel.objects(agents=agentId)
    conversations = [conversation.to_dict() for conversation in models]
    return conversations

def getConversation_resolver(obj, info, id):
    try:
        model = ConversationModel.objects.get(id=id)
        payload = {
            "success": True,
            "conversation": model.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Conversation matching {id} not found"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
