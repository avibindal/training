import sqlite3
# connect to database
conn = sqlite3.connect("mydb.db")
if conn:
    print("connected")
# create a cursor
cursor = conn.cursor()
# define an sql stmt

SQL = """INSERT INTO books values(?,?)"""
mybooks = [("Sam Club","Robin Sharma"),("Misborn","Brandon"),
           ("Two States", "Chetan Bhagat")]
# execute the stmt
cursor.executemany(SQL,mybooks)
print(f"Inserted {cursor.rowcount} rows")
# close cursor
cursor.close()
#commit
conn.commit()
# close connection
conn.close()