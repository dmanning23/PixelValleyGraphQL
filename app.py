from api import app
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, ObjectType
from minimal import PLAYGROUND_HTML
from flask import request, jsonify

from api.queries.scenariosResolver import getScenarios_resolver
from api.queries.scenarioResolver import getScenario_resolver

from api.queries.locationsResolver import getLocationResults_resolver
from api.queries.locationsResolver import getLocations_resolver

query = ObjectType("Query")
query.set_field("scenarios", getScenarios_resolver)
query.set_field("scenario", getScenario_resolver)
query.set_field("locations", getLocationResults_resolver)

scenarios = ObjectType("Scenario")
scenarios.set_field("locations", getLocations_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, [ query, scenarios ]
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