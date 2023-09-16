"""
This script defines base and 
state classes to work with SQLAlchemt ORM
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class States(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): The unique identifier for the state (auto-generated, non-null, primary key).
        name (str): The name of the state (non-null, max length of 128 characters).
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)


