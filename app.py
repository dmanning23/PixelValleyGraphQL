from api import app
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, ObjectType
from minimal import PLAYGROUND_HTML
from flask import request, jsonify

from api.queries.scenarioResolver import getScenarios_resolver
from api.queries.scenarioResolver import getScenario_resolver

from api.queries.locationResolver import getLocationResults_resolver
from api.queries.locationResolver import getLocations_resolver
from api.queries.locationResolver import getLocation_resolver

from api.queries.agentResolver import getScenarioAgents_resolver
from api.queries.agentResolver import getLocationAgents_resolver
from api.queries.agentResolver import getAgentResults_resolver
from api.queries.agentResolver import getAgent_resolver
from api.queries.agentResolver import getAgentDescription_resolver

query = ObjectType("Query")
query.set_field("scenarios", getScenarios_resolver)
query.set_field("scenario", getScenario_resolver)
query.set_field("locations", getLocationResults_resolver)
query.set_field("location", getLocation_resolver)
query.set_field("agents", getAgentResults_resolver)
query.set_field("agent", getAgent_resolver)

scenarios = ObjectType("Scenario")
scenarios.set_field("locations", getLocations_resolver)
scenarios.set_field("agents", getScenarioAgents_resolver)

locations = ObjectType("Location")
locations.set_field("agents", getLocationAgents_resolver)

locations = ObjectType("Agent")
locations.set_field("agentDescription", getAgentDescription_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, [ query, scenarios, locations ]
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code