import MySQLdb as DB
import sys


def cities_list(username, password, db_name, state_name):
    try:
        dabase = DB.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
        )

        cur = dabase.cursor()

        # list = (
        #     "SELECT cities.name"
        #     "FROM cities ORDER BY id ASC"
        #     ""
        #     )

        list = (
            "SELECT DISTINCT cities.name "
            "FROM cities ORDER BY id ASC "
            "WHERE name = %s AND "
            "WHERE cities.state_id = states.id"
            # "JOIN states ON cities.state_id = states.id"
            )

        cur.execute(list, (state_name,))

        cities = cur.fetchall()

        for city in cities:
            print(city)

    except DB.Error as err:
        print("Error: ", err)
    finally:
        cur.close()
        dabase.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    cities_list(username, password, db_name, state_name)
