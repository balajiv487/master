import sqlite3 as sqlite

conn=sqlite.connect("abc.com")
cur=conn.cursor()
s=cur.execute("select * from users")
df=s.fetchall()
print(df)
conn.commit()
conn.close()