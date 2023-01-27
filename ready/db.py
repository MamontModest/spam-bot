import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
try:
    cur.execute("select * from pars ask limit 10")
    print(cur.fetchall())
except:
    pass
try:
    cur.execute("select * from status")
    print(cur.fetchall())
except:
    pass
try:
    cur.execute("select * from stat")
    print(cur.fetchall())
except:
    pass
try:
    cur.execute("select * from spam")
    print(cur.fetchall())
except:
    pass
try:
    cur.execute("select * from line")
    print(cur.fetchall())
except:
    pass
try:
    cur.execute("select * from acaunts")
    print(cur.fetchall())
except:
    pass
try:
    cur.execute("create table stata(suc,no_suc)")
    con.commit()
except:
    pass
try:
    cur.execute("create table acaunts (id_user,api_id,ip_hash,username,proxy)")
    con.commit()
except:
    pass
try:
    cur.execute("create table spam(id_user,message,tg_kanal)")
except:
    pass
try:
    cur.execute("Create table status(id,status)")
except:
    pass
try:
    cur.execute("Create table stat(status,id_creator,tg_kanal)")
except:
    pass
try:
    cur.execute("CREATE TABLE pars(id_creatot,message,tg_kanal,nick)")
except:
    pass
try:
    cur.execute("CREATE TABLE line(tg_kanal)")
except:
    pass
con.commit()




