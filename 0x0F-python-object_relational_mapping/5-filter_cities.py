#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4].strip("'\"")

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    c = db.cursor()
    sql_cmd = "SELECT * FROM cities\
            WHERE state_id = (SELECT id from states\
            WHERE {} = %s)".format("name")
    value = (state_name,)

    c.execute(sql_cmd, value)
    result = c.fetchall()

    j = 0
    for i in result:
        print(i[2], end="")
        if (j != (len(result) - 1)):
            print(", ", end="")
        j = j + 1

    print()

    c.close()
    db.close()
