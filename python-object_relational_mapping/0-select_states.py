import MySQLdb as DB


def states_list(username, password, db_name):
    try:
        dabase = DB.connect(
            host="localhost",
            port="3306",
            user="root",
            passwd="root",
            db="hbtn_0e_0_usa",
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
