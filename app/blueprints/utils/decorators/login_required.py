from functools import wraps
from flask_restx import abort
import flask
import jwt

from app.blueprints.api.controller.user import UserController

controller = UserController()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None

        headers = flask.request.headers
        if "Authorization" in headers:
            token = headers["Authorization"]
        elif "authorization" in headers:
            token = headers["authorization"]
        elif "x-access-token" in headers:
            token = headers["x-access-token"]
        elif "X-Api-Key" in headers:
            token = headers["X-Api-Key"]

        if token is None:
            abort(401, "Token is missing")

        try:
            data = jwt.decode(token, flask.current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = controller.get_user_by_id(data["id"])
        except:
            abort(401, "Token is invalid")

        return f(current_user, *args, **kwargs)

    return decorated_function
