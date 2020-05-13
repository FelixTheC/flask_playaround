#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.05.20
@author: eisenmenger
"""
import sqlalchemy as sa

from app.data.modelbase import SqlAlchemyBase
from datetime import datetime


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, nullable=True, unique=True)
    hashed_password = sa.Column(sa.String, nullable=True, index=True)
    profile_image_url = sa.Column(sa.String)
    last_login = sa.Column(sa.DateTime, default=datetime.now, index=True)
