#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.05.20
@author: eisenmenger
"""
from datetime import datetime
import flask
from flask.views import View, MethodView

from app.utils.response import response

app_bp = flask.Blueprint('home', __name__, template_folder='templates')


def get_dummy_packages():
    return [
        {
            'name': 'flask',
            'version': '1.2.3'
        }, {
            'name': 'sqlalchemy',
            'version': '2.2.0'
        }, {
            'name': 'passlib',
            'version': '3.0.0'
        },
    ]


# @app_bp.route('/')
# @response(template_file='index.html')
# def index():
#     return {'packages': get_dummy_packages()}


# @app_bp.route('/about')
# @response(template_file='about.html')
# def about():
#     return {}

class IndexView(MethodView):
    template_file = 'index.html'

    @response
    def get(self):
        return {'packages': get_dummy_packages()}


class AboutView(MethodView):
    template_file = 'about.html'
    # @response
    # def dispatch_request(self):
    #     print(f'dispatch called: {datetime.today()}')
    #     return {}

    @response
    def get(self):
        print(f'get called: {datetime.today()}')
        return {}


app_bp.add_url_rule('/', view_func=IndexView.as_view(name='index'))
app_bp.add_url_rule('/about', view_func=AboutView.as_view(name='about'))
