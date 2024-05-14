from api.models.journalEntryModel import JournalEntryModel

def getJournalEntryResults_resolver(obj, info, agentId=None):
    try:
        payload = {
            "success": True,
            "journalEntries": getJournalEntries_resolver(obj, info, agentId)
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getJournalEntries_resolver(obj, info, agentId=None):
    #Check if this is coming from the Agent resolver
    if obj is not None:
        agentId = obj["_id"]
    models = JournalEntryModel.objects(agentId=agentId)
    journalEntries = [journalEntry.to_dict() for journalEntry in models]
    return journalEntries

def getJournalEntry_resolver(obj, info, id):
    try:
        model = JournalEntryModel.objects.get(id=id)
        payload = {
            "success": True,
            "journalEntry": model.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["JournalEntry matching {id} not found"]
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
