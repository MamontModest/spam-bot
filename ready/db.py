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
cur.execute("select * from acaunts")
print(cur.fetchall())
cur.execute("create table stata(suc,no_suc)")
con.commit()
cur.execute("create table acaunts (id_user,api_id,ip_hash,username,proxy)")
con.commit()
cur.execute("create table spam(id_user,message,tg_kanal)")
cur.execute("Create table status(id,status)")
cur.execute("Create table stat(status,id_creator,tg_kanal)")
cur.execute("CREATE TABLE pars(id_creatot,message,tg_kanal,nick)")
cur.execute("CREATE TABLE line(tg_kanal)")
con.commit()




