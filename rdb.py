#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2018/12/6
@author: shimakaze-git
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

RDB_PATH = 'sqlite:///db.sqlite3'
ECHO_LOG = True
engine = create_engine(
    RDB_PATH, echo=ECHO_LOG
)
Session = sessionmaker(bind=engine)
session = Session()
