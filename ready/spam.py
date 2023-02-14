import time
import sqlite3
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest,JoinChannelRequest
from telethon.tl.types import InputPeerChannel ,InputUser , InputChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
accs=[]
cur.execute("select * from acaunts")
con.commit()
for i in cur.fetchall():
    accs.append(i)
while True:
    k=0

    for i in accs:
        if k>10:
            break
        else:
            try:
                print(i,i[4])
                username=i[3]
                api_id=int(i[1])
                api_hash=i[2]
                proxy={
                    'proxy_type': 'socks5',
                    'addr': i[4],
                    'port': 1051,
                    'username': 'p64PQH',
                    'password': 'h6yHpv9W12',
                    'rdns': True

                }
                phone=i[0]
                cur.execute("SELECT * FROM pars asc LIMIT 1 ")
                objects = cur.fetchall()
                con.commit()
                client = TelegramClient(username, int(api_id), api_hash, proxy=proxy)
                client.start(phone)
                client(JoinChannelRequest(client.get_entity(objects[0][2])))
                print('add')
                chann = client.get_entity(objects[0][2])
                user=client.get_entity(objects[0][3])
                client(InviteToChannelRequest(chann, [user]))
                client.disconnect()
                print('invite')

                cur.execute("delete from pars where nick=?", [objects[0][3]])
                cur.execute("insert into stata values(0,1)")
                con.commit()
                time.sleep(30)
            except:
                try:
                    cur.execute("delete from pars where nick=?", [objects[0][3]])
                    cur.execute("insert into stata values(1,0)")
                    con.commit()
                    time.sleep(10)
                except:
                    pass


    time.sleep(60*60)



