import mysql.connector

cnx = mysql.connector.MySQLConnection(user='mongouhd_evernorth', password='U*dgQkKRuEHe',
                              host='cp-15.webhostbox.net',
                              database='mongouhd_evernorth',port='3306')
if cnx:
    print("connected")
else:
    print("fail")

cursor=cnx.cursor()
SQL = """Select * from avibooks"""
print(cursor.fetchall())
# execute the stmt
cursor.execute(SQL)
print(f"Inserted {cursor.rowcount} rows")
cnx.commit()
cursor.close()
cnx.close()
