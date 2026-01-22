import sqlite3
# connect to database
conn = sqlite3.connect("mydb.db")
if conn:
    print("connected")
# create a cursor
cursor = conn.cursor()
# define an sql stmt

SQL = """UPDATE books set title = 'JK rowling' where 
author = 'Harry Potter'"""

# execute the stmt
cursor.execute(SQL)
conn.commit()
#get one row
print(cursor.fetchone())
# get multiple rows
print(cursor.fetchmany(2))
# get all rows
print(cursor.fetchall())

# iterate the cursor
for title, author in cursor.execute(SQL):
    print(f"The book {title} was wriiten by {author}")
# close cursor
cursor.close()
# close connection
conn.close()