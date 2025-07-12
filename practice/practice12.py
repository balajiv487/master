import sqlite3

conn=sqlite3.connect("")
cur=conn.cursor()
#cur.execute("select * from table")
conn.commit()
conn.close()

m, n, m, n = [i for i in range(4)]
print(m,n)
print(m + n)