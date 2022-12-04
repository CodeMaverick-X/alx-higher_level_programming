#!/usr/bin/python3
"""
imune to sql injection, because its not passed
directly to the string and i strip and scramble
a bit
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
    sql_cmd = "SELECT * FROM states WHERE {} = %s".format("name")
    value = (state_name,)

    c.execute(sql_cmd, value)
    result = c.fetchall()

    for i in result:
        print(i)

    c.close()
    db.close()
