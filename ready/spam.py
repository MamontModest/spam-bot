import time
import sqlite3
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest,JoinChannelRequest
from telethon.tl.types import InputPeerChannel ,InputUser , InputChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
while True:
    k = 0
    cur.execute("select * from acaunts")
    for i in cur.fetchall():
        k += 1
        if k<=5:
            pass
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
                client = TelegramClient(username, int(api_id), api_hash,proxy=proxy)
                print('connect')
                client.start(phone)

                cur.execute("SELECT * FROM pars asc LIMIT 1 ")
                objects = cur.fetchall()
                client(JoinChannelRequest(objects[0][2]))
                print('joined')
                chann = client.get_entity(objects[0][2])
                lol=client.get_entity(objects[3])
                user = client(ResolveUsernameRequest(lol.username))
                user = InputUser(user.users[0].id, user.users[0].access_hash, )
                client(InviteToChannelRequest(chann.id, [user]))
                print('invite')
                cur.execute("delete from pars where nick=?", [objects[0][3]])
                cur.execute("insert into stata values(1,0)")
                con.commit()
                time.sleep(10)
            except:
                cur.execute("delete from pars where nick=?", [objects[0][3]])
                cur.execute("insert into stata values(0,1)")
                con.commit()
                time.sleep(30)
    time.sleep(60*60*2)



