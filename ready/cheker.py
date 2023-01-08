import configparser
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest,JoinChannelRequest,LeaveChannelRequest
from telethon.functions import messages
from telethon.tl.types import ChannelParticipantsSearch
import random
import sqlite3

config = configparser.ConfigParser()
config.read("config.ini")
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
client = TelegramClient(username, int(api_id), api_hash)
client.start()



def pars_chat(url:str):
    otvet = set()
    otvet2=set()
    offset = 0
    chat_object=client.get_input_entity(url)
    participants = client(GetParticipantsRequest
                          (chat_object.channel_id, ChannelParticipantsSearch(''), offset,
                           hash=chat_object.access_hash, limit=100)
                          )
    print("парсим чат")
    for x in participants.users:
        otvet.add(x.username)
    while participants.users != []:
        participants = client(GetParticipantsRequest
                              (chat_object.channel_id , ChannelParticipantsSearch(''), offset,
                               hash=chat_object.access_hash , limit=100)
                              )
        for x in participants.users:
            otvet.add(x.username)
            otvet2.add(x.id)
        offset += 100
        time.sleep(1 + random.uniform(0, 5))
    with open(str(url.split('/')[-1])+'.txt','w+') as inf:
        for i in otvet:
            inf.write(str(i)+'\n')
    with open(str(url.split('/')[-1])+'2.txt','w+') as inf:
        for i in otvet2:
            inf.write(str(i)+'\n')
    if ceil[-1][0]=='+':
        client(LeaveChannelRequest(chat_object.channel_id))





def pars_channel(url):
    otvet=set()
    chat_object = client.get_input_entity(url)
    print("парсим канал")
    for i in client.get_messages(url, limit=1000):
        try:
            if i.replies.recent_repliers!=None:
                for j in i.replies.recent_repliers:
                    try:
                        otvet.add(j.user_id)
                    except:
                        pass
        except:
            pass
    with open(str(url.split('/')[-1])+'.txt','w+') as inf:
        for i in otvet:
            inf.write(str(i)+'\n')
    if ceil[-1][0]=='+':
        client(LeaveChannelRequest(chat_object.channel_id))





flag=True
while flag==True:
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("select * from line ")
    objects=cur.fetchall()
    print(objects)
    if len(objects)!=0:
        url=objects[0][0]
        ceil = url.split('/')
        if ceil[-1][0] == '+':
            client(messages.ImportChatInviteRequest(ceil[-1][1:]))
        try:
            pars_chat(url)
            cur.execute('delete from line')
            con.commit()
            con.close()
        except:
            pars_channel(url)
            cur.execute('delete from line')
            con.commit()
            con.close()
        time.sleep(20)

    else:
        print('нечего парсить ')
        time.sleep(10)
"""
print(pars_chat('https://t.me/pokerton_chat_ru')) #ok
print(pars_chat('https://t.me/+AJrO31DXmRUwNWRi')) #ok
print(pars_chat("https://t.me/pokerbabyshark")) #ok
print(pars_channel('https://t.me/mvpteam21')) #ok
print(pars_chat(""))
"""
#print(pars_chat(""))
#print(pars_chat(""))


