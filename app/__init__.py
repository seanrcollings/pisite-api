from flask import Flask, jsonify, render_template, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import DevConfig
import json
import sys

db = SQLAlchemy()
migrate = Migrate()

from app.models import Command
from app.api import api


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config)  # load configurations from config object

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(api)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'Command': Command}

    return app
