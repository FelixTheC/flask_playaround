#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.05.20
@author: eisenmenger
"""
import sqlalchemy as sa
from app.data.modelbase import SqlAlchemyBase


class ProgrammingLanguage(SqlAlchemyBase):
    __tablename__ = 'languages'

    description = sa.Column(sa.String)
