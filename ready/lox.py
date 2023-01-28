import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("delete from    acaunts where id_user='79346694500'")
cur.execute("delete from    acaunts where id_user='79587600494'")
cur.execute("delete from    acaunts where id_user='79587600508'")
cur.execute("delete from    acaunts where id_user='79587600704'")
cur.execute("delete from    acaunts where id_user='79587600706'")
con.commit()
