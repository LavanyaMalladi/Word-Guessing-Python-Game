import sqlite3
conn=sqlite3.connect('lav.db')
print("OPENED")
cursor=conn.execute("SELECT * from names")
for row in cursor:
    print (row[0])
row=cursor.fetchall()
name=""
name+=(','.join(row[0]))

#print(row[1])
conn.close()

