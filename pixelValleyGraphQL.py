from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, ObjectType

from ariadne import make_executable_schema
from ariadne.wsgi import GraphQL
from api.queries.scenarioResolver import getScenarios_resolver
from api.queries.scenarioResolver import getScenario_resolver
from api.queries.scenarioResolver import getAgentLocationScenario_resolver
from api.queries.scenarioResolver import getScenarioFromId_resolver

from api.queries.locationResolver import getLocationResults_resolver
from api.queries.locationResolver import getLocations_resolver
from api.queries.locationResolver import getLocation_resolver
from api.queries.locationResolver import getParentLocation_resolver
from api.queries.locationResolver import getChildLocations_resolver
from api.queries.locationResolver import getLocationFromId_resolver

from api.queries.agentResolver import getScenarioAgents_resolver
from api.queries.agentResolver import getScenarioOutsideAgents_resolver
from api.queries.agentResolver import getLocationAgents_resolver
from api.queries.agentResolver import getAgentResults_resolver
from api.queries.agentResolver import getAgent_resolver
from api.queries.agentResolver import getAgentDescription_resolver
from api.queries.agentResolver import getLocationAllAgents_resolver
from api.queries.agentResolver import getConversationInitiatingAgent_resolver
from api.queries.agentResolver import getAgentLocation_resolver
from api.queries.agentResolver import getConversationAgents_resolver

from api.queries.itemResolver import getItem_resolver
from api.queries.itemResolver import getLocationItems_resolver
from api.queries.itemResolver import getAgentItems_resolver

from api.queries.goalResolver import getGoal_resolver
from api.queries.goalResolver import getGoals_resolver

from api.queries.plannedActivityResolver import getPlannedActivity_resolver
from api.queries.plannedActivityResolver import getPlannedActivities_resolver
from api.queries.plannedActivityResolver import getCurrentPlannedActivity_resolver

from api.queries.conversationResolver import getConversation_resolver
from api.queries.conversationResolver import getConversations_resolver

from api.mutations.chatResolver import chatRequest_mutation
from api.mutations.chatResolver import chatResponse_mutation

from api.queries.journalEntryResolver import getJournalEntries_resolver
from api.queries.journalEntryResolver import getJournalEntry_resolver

from api.queries.newspaperResolver import getNewspaper_resolver
from api.queries.newspaperResolver import getNewspapers_resolver
from api.queries.newspaperResolver import getNewspaperResults_resolver

from api.queries.editionResolver import getEditionsResult_resolver
from api.queries.editionResolver import getEdition_resolver
from api.queries.editionResolver import getEditions_resolver

query = ObjectType("Query")
query.set_field("scenarios", getScenarios_resolver)
query.set_field("scenario", getScenario_resolver)
query.set_field("locations", getLocationResults_resolver)
query.set_field("location", getLocation_resolver)
query.set_field("agents", getAgentResults_resolver)
query.set_field("agent", getAgent_resolver)
query.set_field("item", getItem_resolver)
query.set_field("goal", getGoal_resolver)
query.set_field("plannedActivity", getPlannedActivity_resolver)
query.set_field("conversation", getConversation_resolver)
query.set_field("journalEntry", getJournalEntry_resolver)
query.set_field("newspapers", getNewspaperResults_resolver)
query.set_field("newspaper", getNewspaper_resolver)
query.set_field("editions", getEditionsResult_resolver)
query.set_field("edition", getEdition_resolver)

scenarios = ObjectType("Scenario")
scenarios.set_field("locations", getLocations_resolver)
scenarios.set_field("agents", getScenarioAgents_resolver)
scenarios.set_field("outsideAgents", getScenarioOutsideAgents_resolver)
scenarios.set_field("newspapers", getNewspapers_resolver)

newspapers = ObjectType("Newspaper")
newspapers.set_field("editions", getEditions_resolver)

locations = ObjectType("Location")
locations.set_field("agents", getLocationAgents_resolver)
locations.set_field("allAgents", getLocationAllAgents_resolver)
locations.set_field("items", getLocationItems_resolver)
locations.set_field("locations", getChildLocations_resolver)
locations.set_field("parentLocation", getParentLocation_resolver)

agents = ObjectType("Agent")
agents.set_field("agentDescription", getAgentDescription_resolver)
agents.set_field("inventory", getAgentItems_resolver)
agents.set_field("goals", getGoals_resolver)
agents.set_field("plannedActivities", getPlannedActivities_resolver)
agents.set_field("conversations", getConversations_resolver)
agents.set_field("currentActivity", getCurrentPlannedActivity_resolver)
agents.set_field("agentLocation", getAgentLocation_resolver)
agents.set_field("journalEntries", getJournalEntries_resolver)

conversations = ObjectType("Conversation")
conversations.set_field("initiatingAgent", getConversationInitiatingAgent_resolver)
conversations.set_field("agents", getConversationAgents_resolver)
conversations.set_field("scenario", getScenarioFromId_resolver)
conversations.set_field("location", getLocationFromId_resolver)

agentLocations = ObjectType("AgentLocation")
agentLocations.set_field("location", getLocationFromId_resolver)
agentLocations.set_field("scenario", getAgentLocationScenario_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("chatRequest", chatRequest_mutation)
mutation.set_field("chatResponse", chatResponse_mutation)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, [ query, scenarios, locations, agents, conversations, agentLocations, newspapers, mutation ]
)