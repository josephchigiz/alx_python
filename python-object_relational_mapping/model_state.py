"""
Model State Script
"""
from sqlalchemy import create_engine, Column, Integer, String, INT, autoincrement
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
"""
Declarative base.

Parent class for ORM classes to define database tables.
"""


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


username = 'root'
password = 'root'
port = 3306
database = 'hbtn_0e_6_usa'

path = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database)

dabase = create_engine(path)
       

Base.metadata.create_all(dabase)

Session = sessionmaker(bind=dabase)
session = Session()
