#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.05.20
@author: eisenmenger
"""
import sqlalchemy as sa
from app.data.modelbase import SqlAlchemyBase


class Maintainer(SqlAlchemyBase):
    __tablename__ = 'maintainers'

    user_id = sa.Column(sa.Integer, primary_key=True)
    package_id = sa.Column(sa.String, primary_key=True)
