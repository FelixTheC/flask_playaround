#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.05.20
@author: eisenmenger
"""
import sqlalchemy as sa
import sqlalchemy.ext.declarative as dec
from datetime import datetime


class Base:

    @dec.declared_attr
    def __tablename__(cls):
        return f'{cls.__name__.lower()}s'

    id = sa.Column(sa.BigInteger, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.now, index=True)


SqlAlchemyBase = dec.declarative_base(cls=Base)
