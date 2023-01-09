import configparser
import time
import sqlite3
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest,JoinChannelRequest
from telethon.tl.types import InputPeerChannel ,InputUser , InputChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest

config = configparser.ConfigParser()
config.read("config8.ini")
api_id= config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
phone=79317052866
client = TelegramClient(username, int(api_id), api_hash)
client.start(phone)
chann = client.get_entity('https://t.me/rjwmwwlsls')
k=0
while k<14:
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM pars asc LIMIT 1 ")
    objects = cur.fetchall()
    print(objects[0][0])
    try:
        user = client(ResolveUsernameRequest(objects[0][0]))
        user = InputUser(user.users[0].id, user.users[0].access_hash, )
        client(InviteToChannelRequest(chann.id, [user]))
        print('action completted')
        cur.execute("delete from pars where nick=?",[objects[0][0]])
        con.commit()
        k+=1
        time.sleep(60*20)
    except:
        print(objects[0][0],'закрыт инвайт')
        cur.execute("delete from pars where nick=?", [objects[0][0]])
        con.commit()
        time.sleep(100)