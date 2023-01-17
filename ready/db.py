import sqlite3
con = sqlite3.connect("tutorial.db")
cur=con.cursor()
cur.execute("create table spam(id_user,message,tg_kanal)")
cur.execute("Create table status(id,status)")
cur.execute("Create table stat(status,id_creator,tg_kanal)")
cur.execute("CREATE TABLE pars(id_creatot,message,tg_kanal,nick)")
cur.execute("CREATE TABLE line(tg_kanal)")
con.commit()




