import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, INT, autoincrement


username = 'root'
password = 'root'
port = 3306
database = 'hbtn_0e_6_usa'

path = 'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database)

dabase = create_engine(path)

Base = declarative_base


def State(Base):
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name 

