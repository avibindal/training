import sqlite3
# connect to database
conn = sqlite3.connect("mydb.db")
if conn:
    print("connected")
# create a cursor
cursor = conn.cursor()
# define an sql stmt

SQL = """INSERT INTO books values('Wings of fire',
'Harry Potter')"""

# execute the stmt
cursor.execute(SQL)
print(f"Inserted {cursor.rowcount} rows")
# close cursor
cursor.close()
#commit
conn.commit()
# close connection
conn.close()