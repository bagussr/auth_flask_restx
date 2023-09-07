from flask import Blueprint
from flask_restx import Api

bp = Blueprint("api", __name__)
api = Api(bp, version="1.0", title="Masagi - Attendance Services", description="Wargi MASAGI Attendance Service")

from app.blueprints.api import routes
