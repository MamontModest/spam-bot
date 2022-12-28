import configparser
from time import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
config = configparser.ConfigParser()
config.read("config.ini")
api_id= config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
client = TelegramClient(username, int(api_id), api_hash)
client.start()


from telethon.tl.functions.channels import InviteToChannelRequest,JoinChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPeerChannel ,InputUser , InputChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest

spis=['modest72','weawmam']
'''
while True:
	try:
		otvet=set()
		url = input('Ввуди сылку')
		chat_object=client.get_input_entity(url)
		offset = 0
		participants = client(GetParticipantsRequest
							  (chat_object.channel_id, ChannelParticipantsSearch(''), offset,hash=chat_object.access_hash,limit=100)
							  )
		for x in participants.users:
			otvet.add(x.username)

			while participants.users!=[]:
				participants = client(GetParticipantsRequest
									  (chat_object.channel_id, ChannelParticipantsSearch(''), offset,
									   hash=chat_object.access_hash, limit=100)
									  )
				for x in participants.users:
					otvet.add(x.username)
				offset+=100
				time.sleep(1)
		print(len(otvet))
	except:
		print("Чат без прав")









a=input('channel add')
for i in spis[::-1]:
	chann = client.get_entity(a)
	user = client(ResolveUsernameRequest(i))

	user = InputUser(user.users[0].id, user.users[0].access_hash, )
	client(InviteToChannelRequest(chann.id,[user]))
	print('action completted')













for i in spis[::-1]:
	chann = client.get_entity(a)
	print(chann)
	user = client(ResolveUsernameRequest(i))

	user = InputUser(user.users[0].id, user.users[0].access_hash, )
	print(chann,user)
	client(AddChatUserRequest(chann.id,user,1))
	print('action completted')























while True:
	try:
		otvet=set()
		url = input('Ввуди сылку')
		chat_object=client.get_input_entity(url)
		offset = 0
		participants = client(GetParticipantsRequest
							  (chat_object.channel_id, ChannelParticipantsSearch(''), offset,hash=chat_object.access_hash,limit=100)
							  )
		for x in participants.users:
			otvet.add(x.username)

			while participants.users!=[]:
				participants = client(GetParticipantsRequest
									  (chat_object.channel_id, ChannelParticipantsSearch(''), offset,
									   hash=chat_object.access_hash, limit=100)
									  )
				for x in participants.users:
					otvet.add(x.username)
				offset+=100
				time.sleep(1)
		print(len(otvet))
	except:
		print("Чат без прав")



while True:
	url = input('Ввуди сылку')
	for i in client.get_messages(url,limit=10000):
		print(client.get_entity(i.from_id).username)'''

while True :
	url=input('Ввуди сылку')
	for i in client.get_messages(url,limit=1):
		if i.message:
			print(i)
			for j in i.replies.recent_repliers:
				print(client.get_entity(j.user_id).username)