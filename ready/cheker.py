import configparser
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest,JoinChannelRequest,LeaveChannelRequest
from telethon.functions import messages
from telethon.tl.types import ChannelParticipantsSearch
import random
import sqlite3
api_id = '29151876'
api_hash = '2215e64c91e092ae9b9c4a7eb24d6fd6'
username = 'weawmam'
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
        offset += 100
        time.sleep(1 + random.uniform(0, 5))
    with open(str(url.split('/')[-1])+'.txt','w+') as inf:
        for i in otvet:
            inf.write(str(i)+'\n')
    if ceil[-1][0]=='+':
        client(LeaveChannelRequest(chat_object.channel_id))





def pars_channel(url):
    otvet=set()
    chat_object = client.get_input_entity(url)
    print("парсим канал",url)
    for i in client.get_messages(url, limit=5000):
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

