import MySQLdb as DB


def states_list(username, password, db_name):
    try:
        dabase = DB.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
        )

        cur = dabase.cursor()

        list = "SELECT * FROM states ORDER BY id ASC"

        cur.execute(list)

        states = cur.fetchall()

        for state in states:
            print(state)

    except DB.Error:
        print()
    finally:
        cur.close()
        dabase.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <db_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        states_list(username, password, db_name)

# username = root
# password = root
# database = hbtn_0e_0_usa


# cur = dabase.cursor()
# cur.execute("SELECT * FROM states ORDER BY id ASC")

# query_rows = cur.fetchall()
# for row in query_rows:
#     print(row)
# cur.close()
# dabase.close()
