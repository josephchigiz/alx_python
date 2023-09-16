from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    path = "mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1],
        argv[2],
        argv[3])

    engine = create_engine(path)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)


    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
