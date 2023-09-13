import MySQLdb as DB
import sys


def cities_list(username, password, db_name):
    try:
        dabase = DB.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
        )

        cur = dabase.cursor()

        list = (
                    "SELECT MAX(cities.id), cities.name, states.name "
                    "FROM cities "
                    "JOIN states ON cities.state_id = states.id "
                    "GROUP BY cities.name"
                )

        # list = (
        #     "SELECT cities.id, cities.name, states.name "
        #     "FROM (SELECT DISTINCT name, state_id FROM cities) cities "
        #     "JOIN states ON cities.state_id = state_id"
        #     )

        cur.execute(list)

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
    cities_list(username, password, db_name)
