import configparser
import time
import pandas as pd
import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.channels import InviteToChannelRequest,JoinChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPeerChannel ,InputUser , InputChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest
import random


config = configparser.ConfigParser()
config.read("config.ini")
api_id= config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
client = TelegramClient(username, int(api_id), api_hash)
client.start()

def pars_chat(url:str):
    otvet = set()
    offset = 0
    chat_object=client.get_input_entity(url)
    participants = client(GetParticipantsRequest
                          (chat_object.channel_id, ChannelParticipantsSearch(''), offset,
                           hash=chat_object.access_hash, limit=100)
                          )
    for x in participants.users:
        otvet.add(x.username)
    while participants.users != [] and len(otvet)<500:
        participants = client(GetParticipantsRequest
                              (chat_object.channel_id , ChannelParticipantsSearch(''), offset,
                               hash=chat_object.access_hash , limit=100)
                              )
        for x in participants.users:
            otvet.add(x.username)
        offset += 100
        time.sleep(1 + random.uniform(0, 2))
    print(url.split('/')[-1])
    with open(str(url.split('/')[-1])+'.txt','w+') as inf:
        for i in otvet:
            inf.write(str(i)+'\n')



def pars_cnahhel(url:str):
    otvet=set()
    for i in client.iter_messages(url,limit=1):
        print(i.replises)

pars_cnahhel('https://t.me/postypashki_old')























'''config = configparser.ConfigParser()
config.read("config.ini")
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
client = TelegramClient(username, int(api_id), api_hash)
client.start()
client.log_out()
'''