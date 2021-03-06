#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.05.20
@author: eisenmenger
"""
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app.data.modelbase import SqlAlchemyBase
from app.data.releases import Release


class Package(SqlAlchemyBase):
    __tablename__ = 'packages'

    package_id = sa.Column(sa.String, primary_key=True)
    summary = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)

    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String, index=True)

    license = sa.Column(sa.String, index=True)

    releases = orm.relation('Release', order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc(),
    ], back_populates='package')

    def __repr__(self):
        return f'<Package: {self.package_id}>'
