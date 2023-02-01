import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("delete from acaunts")
con.commit()
'''
cur.execute("insert into   acaunts values('79587600803','26578549','c5416d38d16ef47a8e38b753fb39d2ed','dfgfdgdf','185.181.244.190')")
cur.execute("insert into   acaunts values('79871857168','20213259','dc0a074aa4458ca4ba548f454a5fe833','gsgsgs','188.130.128.171')")
cur.execute("insert into   acaunts values('79587600797','24856625','993ee1ab47266eca7c1c5195471c9fd8','dagyjfhd','109.248.205.82')")
cur.execute("insert into   acaunts values('79587600494','28623916','4be346a285b94c23a65f96141fc0ffaf','clients123dsa','188.130.128.171')")
cur.execute("insert into   acaunts values('79346694500','26522332','3758dae2bbd9cc280e11269385a2e421','kolkoad','188.130.128.171')")
cur.execute("insert into   acaunts values('79587600706','21165605','1df6e22ce5e5969f5089d19c4d502c67','kgismmgs1','109.248.205.82')")
cur.execute("insert into   acaunts values('79587600804','29667385','dc45eefea1fd26922b9076bee96d242b','daaskosvs','185.181.244.190')")
cur.execute("insert into   acaunts values('79587600508','26522332','3758dae2bbd9cc280e11269385a2e421','kfoal2ms','188.130.128.171')")
cur.execute("insert into   acaunts values('79587600804','29667385','dc45eefea1fd26922b9076bee96d242b','daaskosvs','185.181.244.190')")
cur.execute("insert into   acaunts values('79874216191','26104265','f856d7e27cf19cb7486279fb3a3ba9f8','adhghdhdf','109.248.205.82')")
cur.execute("insert into   acaunts values('79912484309','18211331','ff767bad55e0a57496eb40b662a9d77d','fdfsdgdsfsdf','109.248.205.82')")
cur.execute("insert into   acaunts values('79913929496','24158678','8d506001d6ac4c4b68e97dc0b0f2247a','dagfsgsg','109.248.205.82')")
cur.execute("insert into   acaunts values('79915670820','21312944','9ec1577d80a3bad0cc82442cdf8ac64d','dasgfgdf','109.248.205.82')")
'''
cur.execute("insert into   acaunts values('79809341730','23567633','10056ac1034d0abdbd3a094de520ca86','wqefdfhtydh','185.181.244.190')")
cur.execute("insert into   acaunts values('79587600807','13894654','bfa8bdc0e3a08c19f7abde4db3945df1','dafghth','185.181.244.190')")
cur.execute("insert into   acaunts values('79587600906','24220542','7511dd65d44c964e48939b01dec8b556','gskfgismmfs','185.181.244.190')")
cur.execute("insert into   acaunts values('79915678602','27472245','2069b82088da9cffd1f5b757315ea0af','hfghfghdfgsg','185.181.244.190')")
cur.execute("insert into   acaunts values('79809341733','25152860','eec604b78cf21f0ba9ca4a56c7ee07e0','fgsdsdsdf','188.130.128.171')")
cur.execute("insert into   acaunts values('79809341751','20775856','783ae73f7cda186daa241cc434d13f41','dfgdgdfe','188.130.128.171')")


con.commit()