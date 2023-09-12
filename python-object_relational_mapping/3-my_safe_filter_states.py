import MySQLdb as DB
import sys


def states_list(username, password, db_name, new_safe_state):
    try:
        dabase = DB.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
        )

        cur = dabase.cursor()

        query = (
            "SELECT * FROM states WHERE name = %s "
            "AND name LIKE 'N%' COLLATE utf8mb4_bin"
            )

        cur.execute(query, (new_safe_state,))

        states = cur.fetchall()

        for state in states:
            print(state)

    except DB.Error:
        print()
    finally:
        cur.close()
        dabase.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    new_safe_state = sys.argv[4]
    states_list(username, password, db_name, new_safe_state)
