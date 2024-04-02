import os
from ariadne.wsgi import GraphQL
from pixelValleyGraphQL import schema

application = GraphQL(schema)