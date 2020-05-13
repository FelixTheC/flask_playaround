#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.05.20
@author: eisenmenger
"""
from app.data.modelbase import SqlAlchemyBase
import sqlalchemy as sa


class License(SqlAlchemyBase):
    __tablename__ = 'licenses'

    description = sa.Column(sa.String)
