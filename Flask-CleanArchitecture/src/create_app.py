from flask import Flask, redirect, url_for
from flask_admin import Admin
from flask_admin import AdminIndexView
from config import Config
from .api.middleware import setup_middleware
from .api.routes import register_routes
from .infrastructure.databases import init_db
from .app_logging import setup_logging
from api.controllers.admin_controller import admin_bp 


def create_app():
    app.template_folder = 'views'
    app = Flask(__name__)
    app.config.from_object(Config)


    setup_logging(app)
    init_db(app)
    setup_middleware(app)
    register_routes(app)
    app.register_blueprint(admin_bp)

    return app