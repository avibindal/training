import mysql.connector

cnx = mysql.connector.MySQLConnection(user='mongouhd_evernorth', password='U*dgQkKRuEHe',
                              host='cp-15.webhostbox.net',
                              database='mongouhd_evernorth',port='3306')
if cnx:
    print("connected")
else:
    print("fail")

cursor=cnx.cursor()
SQL = """INSERT INTO avibooks (title,author) values(%s,%s)"""
mybooks = [("Sam Club","Robin Sharma"),("Misborn","Brandon"),
           ("Two States", "Chetan Bhagat")]
# execute the stmt
cursor.executemany(SQL,mybooks)
print(f"Inserted {cursor.rowcount} rows")
cnx.commit()
cursor.close()
cnx.close()
