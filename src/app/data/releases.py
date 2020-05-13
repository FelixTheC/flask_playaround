#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.05.20
@author: eisenmenger
"""
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app.data.modelbase import SqlAlchemyBase


class Release(SqlAlchemyBase):
    __tablename__ = 'releases'

    major_ver = sa.Column(sa.BigInteger, index=True)
    minor_ver = sa.Column(sa.BigInteger, index=True)
    build_ver = sa.Column(sa.BigInteger, index=True)

    comment = sa.Column(sa.String)
    url = sa.Column(sa.String)
    size = sa.Column(sa.String)

    package_id = sa.Column(sa.String, sa.ForeignKey(column='packages.package_id'))
    package = orm.relation('Package')

    @property
    def version_str(self):
        return f'{self.major_ver}.{self.minor_ver}.{self.build_ver}'
