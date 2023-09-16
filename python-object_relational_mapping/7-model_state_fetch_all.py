from sqlalchemy import create_engine, Column, String, Integer
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def states_list(username, password, port, db):
    path = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, db)

    engine = create_engine(path)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    states_list(username, password, db)
