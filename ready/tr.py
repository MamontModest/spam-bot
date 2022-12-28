import configparser
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import random
from telethon.tl.functions.channels import GetParticipantsRequest,JoinChannelRequest,LeaveChannelRequest
import sqlite3






con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("select * from line ")
con.commit()
objects=cur.fetchall()
print(objects)




