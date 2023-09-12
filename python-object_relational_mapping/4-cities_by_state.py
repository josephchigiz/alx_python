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

        list = "SELECT * FROM cities ORDER BY id ASC"

        cur.execute(list)

        cities = cur.fetchall()

        for city in cities:
            print(city)

    except DB.Error:
        print()
    finally:
        cur.close()
        dabase.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    cities_list(username, password, db_name)