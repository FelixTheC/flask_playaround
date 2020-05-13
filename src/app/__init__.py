#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.05.20
@author: eisenmenger
"""
import flask
import pathlib

from app.data import db_session
from app.utils.register_blueprints import add_blueprints_from_dir

flask_app = flask.Flask(__name__)


def register_blueprints(used_flask_app: any):
    current = pathlib.Path.cwd()
    add_blueprints_from_dir(directory=pathlib.Path.joinpath(current, 'src', 'app', 'views'),
                            flask_app=used_flask_app)
    # from app.views import home_views
    # from app.views import package_views
    # used_flask_app.register_blueprint(home_views.app_bp)
    # used_flask_app.register_blueprint(package_views.app_bp)


def setup_db():
    current = pathlib.Path.cwd()
    db_file = pathlib.Path.joinpath(current, 'src', 'app', 'db', 'pypi.sqlite3')
    db_session.global_init(db_file.as_posix())


@flask_app.template_filter()
def filter_context(context, value):
    return context
