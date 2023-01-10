import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("select * from spam")
print(cur.fetchall())
cur.execute("select * from status")
print(cur.fetchall())
cur.execute("select * from stat")
print(cur.fetchall())
cur.execute("select * from pars")
print(cur.fetchall())
cur.execute("select * from line")
print(cur.fetchall())
cur.execute("create table spam(id_user,message,tg_kanal)")
cur.execute("Create table status(id,status)")
cur.execute("Create table stat(status,id_creator,tg_kanal)")
cur.execute("CREATE TABLE pars(nick,channel)")
cur.execute("CREATE TABLE line(tg_kanal)")
con.commit()




