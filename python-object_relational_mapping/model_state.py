from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
"""
The declarative base.

It is used as a parent class
"""
class State(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int):
        name (str): 
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name =  Column(String(128), nullable=False)