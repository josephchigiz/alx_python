import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, INT, autoincrement
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
    """
    declarative class doctring
    """

class State(Base):
     """
     docstring for State
     """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    """
    this is a unique identifier for the state
    """

    name = Column(String(128), nullable=False)
    """
    This is the name of the state
    """

username = 'root'
password = 'root'
port = 3306
database = 'hbtn_0e_6_usa'

path = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database)

dabase = create_engine(path)
       

Base.metadata.create_all(dabase)

Session = sessionmaker(bind=dabase)
session = Session()
