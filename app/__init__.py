from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)
    app.config["CORS_HEADERS"] = ["Content-Type", "Authorization"]
    CORS(app, resources={r"/api/*": {"origins": "*", "supports_credentials": True}})

    from app.blueprints.api import bp as api_v1

    CORS(api_v1, resources={r"/api/*": {"origins": "*", "supports_credentials": True}})
    app.register_blueprint(api_v1, url_prefix="/api/v1")

    @app.get("/")
    def index():
        return redirect(url_for("api.doc"))

    return app


from app import models
