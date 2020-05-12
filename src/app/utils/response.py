#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.05.20
@author: eisenmenger
"""
from functools import wraps

import flask


def response(_func=None, *, mimetype: str = None, template_file: str = None):

    def wrapper(func):

        @wraps(func)
        def view_method(*args, **kwargs):
            response_val = func(*args, **kwargs)
            if isinstance(response_val, flask.Response):
                return response_val

            if template_file is not None:
                tf = template_file
            else:
                try:
                    tf = getattr(args[0], 'template_file')
                except (IndexError, AttributeError):
                    tf = None

            if tf and not isinstance(response_val, dict):
                raise Exception(
                    f'Invalid return type {type(response_val)}, expected was a dict as return value'
                )

            if tf:
                response_val = flask.render_template(tf, **response_val)

            resp = flask.make_response(response_val)
            if mimetype:
                resp.mimetype = mimetype

            return resp
        return view_method

    if _func is not None:
        return wrapper(_func)
    return wrapper
