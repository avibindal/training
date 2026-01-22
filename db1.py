import sqlite3
# connect to database
conn = sqlite3.connect("mydb.db")
if conn:
    print("connected")
# create a cursor
cursor = conn.cursor()
# define an sql stmt

SQL = """CREATE TABLE books(
title TEXT,
author TEXT)"""

# execute the stmt
cursor.execute(SQL)
# close cursor
cursor.close()
# close connection
conn.close()