#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.05.20
@author: eisenmenger
"""
import sqlalchemy as sa
from app.data.modelbase import SqlAlchemyBase


class Download(SqlAlchemyBase):

    package_id = sa.Column(sa.String, index=True)
    release_id = sa.Column(sa.BigInteger, index=True)

    ip_address = sa.Column(sa.String)
    user_agent = sa.Column(sa.String)
