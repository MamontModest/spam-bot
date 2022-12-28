import configparser
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import ChannelParticipantsSearch, InputUser
import random
import sqlite3
config = configparser.ConfigParser()
config.read("config.ini")
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
client = TelegramClient(username, int(api_id), api_hash)
client.start()
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
client.log_out()
client = TelegramClient(username, int(api_id), api_hash)
client.start()




def invite_to_chat(nickname,url):
    chann = client.get_entity(url)
    user = client(ResolveUsernameRequest(nickname))
    user = InputUser(user.users[0].id, user.users[0].access_hash, )
    client(AddChatUserRequest(chann.id, user, 1))
    print('action completted')

flag=True
while flag==True:
    cur.execute("select * from pars ")
    objects=cur.fetchall()
    invite_to_chat(objects[0][0],objects[0][1])
    time.sleep(180)
    print('error')
    time.sleep(10)