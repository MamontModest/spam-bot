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
config = configparser.ConfigParser()
config.read("config.ini")
api_id= config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
client = TelegramClient(username, int(api_id), api_hash)
def pars_chat(url:str):
    otvet = set()
    offset = 0
    participants = client(GetParticipantsRequest
                          (client.start().get_input_entity(url).channel_id, ChannelParticipantsSearch(''), offset,
                           hash=client.start().get_input_entity(url).access_hash, limit=100)
                          )
    for x in participants.users:
        otvet.add(x.username)
    print(otvet)
print(pars_chat('https://t.me/+OsKnLNG-7DE1ZTFi'))



























"print(pars_chat('https://t.me/+OsKnLNG-7DE1ZTFi'))"
'''while participants.users != []:
            participants = client(GetParticipantsRequest
                                  (chat_object.channel_id, ChannelParticipantsSearch(''), offset,
                                   hash=chat_object.access_hash, limit=100)
                                  )
            for x in participants.users:
                otvet.add(x.username)
            offset += 100
            time.sleep(1+random.uniform(0,2))'''

'''config = configparser.ConfigParser()
config.read("config.ini")
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
client = TelegramClient(username, int(api_id), api_hash)
client.start()
client.log_out()
'''