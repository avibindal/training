import mysql.connector

cnx = mysql.connector.MySQLConnection(user='mongouhd_evernorth', password='U*dgQkKRuEHe',
                              host='cp-15.webhostbox.net',
                              database='mongouhd_evernorth',port='3306')
if cnx:
    print("connected")
else:
    print("fail")

cursor=cnx.cursor()
SQL= """CREATE TABLE avibooks(
title TEXT,
author TEXT)"""
cursor.execute(SQL)
cnx.commit()
cursor.close()
cnx.close()
