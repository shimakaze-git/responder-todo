#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''
import os
from datetime import datetime

from rdb import Base
from rdb import engine

from sqlalchemy import Column, String, DateTime, text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER

SQLITE3_NAME = "./db.sqlite3"


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    name = Column(String(256))
    text = Column(String(256))
    created_at = Column(
        DateTime,
        nullable=False,
        server_default=current_timestamp()
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        onupdate=datetime.now
        # server_default=text(
        #     'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'
        # )
    )

if __name__ == "__main__":
    path = SQLITE3_NAME
    if not os.path.isfile(path):
        # テーブル作成
        Base.metadata.create_all(engine)
