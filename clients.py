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
    with open(url.split('/')[-1]+'.txt','w+') as inf:
        for i in otvet:
            inf.write(i+'\n')

print(pars_chat("https://t.me/botalkaaa"))






def pars_channel(url:str):
	for i in client.get_messages(url,limit=1):
		if i.message:
			print(i)
			for j in i.replies.recent_repliers:
				print(client.get_entity(j.user_id).username)

























'''config = configparser.ConfigParser()
config.read("config.ini")
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
client = TelegramClient(username, int(api_id), api_hash)
client.start()
client.log_out()
'''