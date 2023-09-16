from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    path = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1],
        argv[2],
        argv[3])

    engine = create_engine(path)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_list = session.query(State).order_by(State.id).all()
    for state in state_list:
        print("{}: {}".format(state.id, state.name))
    session.close()
