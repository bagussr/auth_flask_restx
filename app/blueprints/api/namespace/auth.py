from flask_restx import Namespace, Resource, fields, abort
import flask

from app.blueprints.api.serialize.user import UserSchema
from app.blueprints.api.controller.user import UserController
from app.blueprints.utils.decorators.login_required import login_required

authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}}

ns = Namespace("auth", description="Authentication related operations", authorizations=authorizations)

user = ns.model(
    "UserRequest",
    {
        "username": fields.String(required=True),
        "password": fields.String(required=True),
    },
)
controller = UserController()


@ns.route("/")
@ns.doc(security="apikey")
class IndexAuth(Resource):
    method_decorators = [login_required]

    def get(self, current_user):
        return UserSchema().dump(current_user), 200


@ns.route("/login")
class LoginAuth(Resource):
    @ns.expect(user, validate=True)
    def post(self):
        data = ns.payload
        user = controller.get_user_by_username(data.get("username"))

        if user is None:
            abort(401, "User not found")

        if user.password_hash != data.get("password"):
            abort(401, "Password is invalid")

        token = controller.create_token(user, flask.current_app.config["SECRET_KEY"])
        return {"message": "Login success", "token": token}, 200


@ns.route("/register")
class RegisterAuth(Resource):
    @ns.expect(ns.inherit("UserRegister", user, {"name": fields.String(required=True)}), validate=True)
    def post(self):
        data = ns.payload
        try:
            controller.create_user(data.get("name"), data.get("username"), data.get("password"))
            return {"message": "User created"}, 201
        except Exception as e:
            return {"message": str(e)}, 400
