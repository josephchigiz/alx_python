import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, INT, autoincrement
from sqlalchemy.orm import sessionmaker

username = 'root'
password = 'root'
port = 3306
database = 'hbtn_0e_6_usa'

path = 'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database)

dabase = create_engine(path)

Base = declarative_base

class State(object):
     """docstring for State"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

        

