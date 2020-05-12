#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.05.20
@author: eisenmenger
"""
import flask
from flask.views import MethodView

from app.utils.response import response

app_bp = flask.Blueprint('account', __name__, template_folder='templates', url_prefix='/account')


# ################ INDEX ######################

@app_bp.route('/')
@response(template_file='account/index.html')
def index():
    return {}


# ################ REGISTER ####################


class RegisterView(MethodView):
    template_file = 'account/register.html'

    @response
    def get(self):
        return {}

    @response
    def post(self):
        return {}


# ################ LOGIN ######################

class LoginView(MethodView):
    template_file = 'account/login.html'

    @response
    def get(self):
        return {}

    @response
    def post(self):
        return {}


# ################ LOGOUT ######################

@app_bp.route('/logout')
@response(template_file='account/logout.html')
def logout():
    return {}


app_bp.add_url_rule('/register', view_func=RegisterView.as_view(name='register'))
app_bp.add_url_rule('/login', view_func=LoginView.as_view(name='login'))
