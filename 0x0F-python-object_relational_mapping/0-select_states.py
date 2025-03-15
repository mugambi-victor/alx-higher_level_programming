#!/usr/bin/python3
# Script to list all states from the db hbtn_0e_0_usa
# Usage ./0-select_states.py <mysql_username> <mysql_password> <database_name>

import sys
import MySQLdb

if __name__ == "__main__":
    # obtain mysql credentials from the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect to server
    db = MySQLdb.connect(host="localhost", user=username,
                         password=password,
                         db=database, port=3306)
    cursor = db.cursor()

    # query to retrieve states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    # print
    for state in states:
        print(state)

    # close cursor and db connection
    cursor.close()
    db.close()
