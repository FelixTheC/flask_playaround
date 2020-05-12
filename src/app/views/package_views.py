#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.05.20
@author: eisenmenger
"""
import flask
from flask.views import MethodView

from app.utils.response import response

app_bp = flask.Blueprint('package', __name__, template_folder='templates')


@app_bp.route('/package/<package_name>')
@response(template_file='packages/details.html')
def package_details(package_name: str):
    return {'package': package_name}


# @app_bp.route('/<int:rank>')
# @response(template_file='packages/details.html')
# def popular(rank: int):
#     return {'package': rank}


class PopularAPI(MethodView):
    template_file = 'packages/details.html'

    def get(self, rank: int):
        return self.render_response('_get', rank=rank)

    @response
    def render_response(self, response_type: str, **kwargs):
        return getattr(self, response_type)(**kwargs)

    def _get(self, rank: int):
        return {'package': rank}


popular_view = PopularAPI.as_view(name='popular')
app_bp.add_url_rule('/<int:rank>', view_func=popular_view, methods=['GET', ])
