from app.blueprints.api import api
from app.blueprints.api.namespace.auth import ns

api.add_namespace(ns)
