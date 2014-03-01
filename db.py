# -*- coding: utf-8 -*- 

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import datetime



verbose=False #Set to True to enable verbose
engine = create_engine('sqlite:///database', echo=verbose)
Base = declarative_base()


#SMS class
class Note(Base):
    __tablename__ = 'notes'

    #Id table
    id = Column(Integer, primary_key=True)

    #Note field
    note = Column(String(100))

    #Date
    date =  Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Note(note='%s')>" % (self.text)


Base.metadata.create_all(engine)