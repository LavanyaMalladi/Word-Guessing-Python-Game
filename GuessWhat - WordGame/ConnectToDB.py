import sqlite3
conn=sqlite3.connect('lav.db')
print("OPENED")
conn.execute("""CREATE TABLE names
                  (name text) 
               """)
#conn.execute("CREATE TABLE student1(NAME varchar(20))")
print("CREATED")
conn.close()
