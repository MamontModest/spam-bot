import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("Create table stat(status)")
con.commit()
cur.execute("CREATE TABLE pars(nick,channel)")
cur.execute("CREATE TABLE line(tg_kanal)")
con.commit()
