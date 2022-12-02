#!/usr/bin/python3
"""connect to mysql server and qet data from cites table"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    c = db.cursor()
    sql_cmd = "SELECT * FROM cities ORDER BY id ASC"

    c.execute(sql_cmd)
    result = c.fetchall()

    for i in result:
        print(i)

    c.close()
    db.close()
