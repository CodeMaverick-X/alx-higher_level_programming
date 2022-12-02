#!/usr/bin/python3
"""connect to mysql server and qet data"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    c = db.cursor()


    c.execute("SELECT * FROM states WHERE name = %s", (state_name,))
    result = c.fetchall()

    for i in result:
        print(i)

    c.close()
    db.close()
