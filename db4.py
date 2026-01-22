import sqlite3
# connect to database
conn = sqlite3.connect("mydb.db")
if conn:
    print("connected")
# create a cursor
cursor = conn.cursor()
# define an sql stmt

SQL = """Select * from books"""

# execute the stmt
cursor.execute(SQL)
#get one row
print(cursor.fetchone())
# get multiple rows
print(cursor.fetchmany(1))
# get all rows
print(cursor.fetchall())

# iterate the cursor
for title, author in cursor.execute(SQL):
    print(f"The book {title} was wriiten by {author}")
# close cursor
cursor.close()
# close connection
conn.close()