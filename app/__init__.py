from flask import Flask
from config import app_config
from app.api.model.db import db_init
from app.api.view.cases import globalUpdatesBlueprint as cases_blueprint


def create_app(the_configuration):
    """This is where the app is created for this application"""
    app = Flask(__name__)
    app.config.from_object(app_config[the_configuration])
    app.app_context().push()
    app.register_blueprint(cases_blueprint)
    if the_configuration != "testing":
        db_init()
    return app